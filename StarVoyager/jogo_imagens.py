from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, CardMaker
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
import random

class StarVoyager(ShowBase):

    def __init__(self):
        super().__init__()

        win_props = WindowProperties()
        win_props.setSize(1280, 720)
        self.win.requestProperties(win_props)
        self.set_background_color(0, 0, 0)

        self.disable_mouse()
        self.camera.set_pos(0, -20, 5)
        self.camera.set_hpr(0, -10, 0)

        self.player = self.create_sprite("spaceship.png")
        self.player.reparent_to(self.render)
        self.player.set_pos(0, 0, -1)

        self.accept("arrow_left", self.move_player, [-1])
        self.accept("arrow_right", self.move_player, [1])

        self.enemies = []
        self.stars = []

        self.taskMgr.add(self.spawn_ememy, "SpawnEnemyTask")
        self.taskMgr.add(self.spawn_star, "SpawnStarTask")
        self.taskMgr.add(self.update_game, "UpdateGameTask")

        self.score = 0
        self.display_score()

    def create_sprite(self, image_path, scale = 1):
        cm = CardMaker("sprite")
        cm.set_frame(-1, 1, -1, 1)
        sprite = self.render.attach_new_node(cm.generate())
        texture = self.loader.load_texture(image_path)
        sprite.set_texture(texture, 1)
        sprite.set_scale(scale)

    def move_player(self, direction):
        pos = self.player.get_x()
        if (-9 < pos + direction < 9):
            self.player.set_x(pos + direction)

    def spawn_ememy(self, task):
        if random.random() < 0.01:
            enemy = self.create_sprite("asteroid.png", scale = 1)
            enemy.reaparent_to(self.render)
            enemy.set_pos(random.uniform(-7, 7), random.uniform(5, 15), 0)
            self.enemies.append(enemy)
        return Task.cont
    
    def spawn_star(self, task):
        if random.random() < 0.02:
            star = self.create_sprite("star.png", scale = 0.5)
            star.reaparent_to(self.render)
            star.set_pos(random.uniform(-7, 7), random.uniform(5, 15), 0)
            self.stars.append(star)
        return Task.cont
    
    def dsiplay_score(self):
        if hasattr(self, "score text"):
            self.score_text.destroy()
        self.score_text = OnscreenText(text = f"Score: {self.score}", pos = (-1.75, 0.9), scale = 0.07, fg = (1, 1, 1, 1))

    def update_game(self, task):
        for emeny in self.enemies[:]:
            emeny.set_y(enemy.get_y() - 0.1)
            if (enemy.get_y() < -5):
                enemy.remove_node()
                self.enemies.remove(enemy)

        for star in self.stars[:]:
            star.set_y(star.get_y() - 0.1)
            if (star.get_y() < -5):
                star.remove_node()
                self.stars.remove(star)

        for star in self.stars[:]:
            if ((self.player.get_pos() - star.get_pos()).lengt() < 1.5):
                star.remove_node()
                self.stars.remove(star)
                self.score += 1
                self.dsiplay_score
        return Task.cont

app = StarVoyager
app.run()
