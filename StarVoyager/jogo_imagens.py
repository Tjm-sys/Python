from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, CardMaker, LVector3
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectButton import DirectButton
import random

class StarVoyager(ShowBase):

    def __init__(self):
        super().__init__()

        win_props = WindowProperties()
        win_props.setSize(1280, 720)
        self.win.requestProperties(win_props)

        self.create_screen_start("Start.png")

        self.accept("arrow_left", self.move_player, [-1])
        self.accept("arrow_right", self.move_player, [1])

        self.game_started = False
        self.enemies = []
        self.stars = []
        self.player = None

    def set_background_image(self, image_path):
        cm = CardMaker("background")
        cm.setFrame(-1, 1, -1, 1)
        self.background = self.render2d.attachNewNode(cm.generate())
        texture = self.loader.load_texture(image_path)        
        self.background.setTexture(texture)

    def start_game(self):
        self.game_started = True
        self.score = 0
        self.button.hide()
        self.background.remove_node()
        self.set_background_color(0, 0, 0)

        self.disable_mouse()
        self.camera.set_pos(0, -20, 5)
        self.camera.set_hpr(0, -10, 0)

        self.player = self.create_sprite("spaceship.png")
        self.player.reparent_to(self.render)
        self.player.set_pos(0, 0, -1)
        
        self.taskMgr.add(self.spawn_enemy, "SpawnEnemyTask")
        self.taskMgr.add(self.spawn_star, "SpawnStarTask")
        self.taskMgr.add(self.update_game, "UpdateGameTask")

    def clear_game(self):

        self.taskMgr.remove("SpawnEnemyTask")
        self.taskMgr.remove("SpawnStarTask")
        self.taskMgr.remove("UpdateGameTask")

        if hasattr(self, "background"):
            self.background.remove_node()

        if hasattr(self, "score_text"):
            self.score_text.destroy()
        
        if hasattr(self, "button"):
            self.button.hide()

    def play_music(self, file_name, loop = True, volume = 0.3):
        self.music = self.loader.loadMusic(file_name)
        self.music.setLoop(loop)
        self.music.setVolume(volume)
        self.music.play()

    def create_screen_start(self, image_path):
        self.clear_game()
        self.set_background_image(image_path)
        self.play_music("space.ogg")
        self.button = DirectButton(text = ("Start",), scale = 0.1, pos = (0, 0, -0.4), command = self.start_game, frameColor = (0.8, 0.8, 0.8, 1))

    def create_screen(self, image_path):
        self.clear_game()
        self.set_background_image(image_path)
        self.button = DirectButton(text = ("Play again",), scale = 0.1, pos = (0, 0, -0.4), command = lambda: self.create_screen_start("Start.png"), frameColor = (0.8, 0.8, 0.8, 1))

    def create_sprite(self, image_path, scale = 1):
        cm = CardMaker("sprite")
        cm.set_frame(-1, 1, -1, 1)
        sprite = self.render.attach_new_node(cm.generate())
        texture = self.loader.load_texture(image_path)
        sprite.set_texture(texture, 1)
        sprite.set_scale(scale)
        return sprite

    def move_player(self, direction):
        pos = self.player.get_x()
        if (-9 < pos + direction < 9):
            self.player.set_x(pos + direction)

    def spawn_enemy(self, task):
        if random.random() < 0.01:
            enemy = self.create_sprite("asteroid.png", scale = 1)
            enemy.reparent_to(self.render)
            enemy.set_pos(random.uniform(-7, 7), random.uniform(5, 15), 0)
            self.enemies.append(enemy)
        return Task.cont
    
    def spawn_star(self, task):
        if random.random() < 0.02:
            star = self.create_sprite("star.png", scale = 0.5)
            star.reparent_to(self.render)
            star.set_pos(random.uniform(-7, 7), random.uniform(5, 15), 0)
            self.stars.append(star)
        return Task.cont
    
    def display_score(self):
        if hasattr(self, "score_text"):
            self.score_text.destroy()
        self.score_text = OnscreenText(text = f"Score: {self.score}", pos = (-1.75, 0.9), scale = 0.07, fg = (1, 1, 1, 1))
    
    def update_game(self, task):
        if not self.game_started:
            return Task.cont

        if self.score >= 5:
            self.game_started = False

            if hasattr(self, "player"):
                self.player.hide()
            self.create_screen("Win.png")

        for enemy in self.enemies[:]:
            enemy.set_y(enemy.get_y() - 0.1)
            if (enemy.get_y() < -5):
                enemy.remove_node()
                self.enemies.remove(enemy)

        for star in self.stars[:]:
            star.set_y(star.get_y() - 0.1)
            if (star.get_y() < -5):
                star.remove_node()
                self.stars.remove(star)

        for star in self.stars[:]:
            if ((self.player.get_pos() - star.get_pos()).length() < 1.5):
                star.remove_node()
                self.stars.remove(star)
                self.score += 1
                self.display_score()
        for enemy in self.enemies[:]:
            if (self.player.get_pos() - enemy.get_pos()).length() < 1.5:
                enemy.remove_node()
                self.enemies.remove(enemy)
                self.score -= 1
                self.display_score()
            
            if self.score < 0:
                self.game_started = False

                if hasattr(self, "player"):
                    self.player.hide()
                self.create_screen("Game Over.png")

            
        return Task.cont

app = StarVoyager()
app.run()
