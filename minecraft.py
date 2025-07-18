# Importações matemáticas básicas
from math import pi, sin, cos

# Importações do Panda3D
from direct.showbase.ShowBase import ShowBase  # Classe base para criar janelas e renderização
from direct.task import Task  # Para criar tarefas que são executadas a cada frame
from direct.gui.OnscreenImage import OnscreenImage  # Para exibir imagens na tela (como mira)

# Componentes gráficos e de colisão
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight, AmbientLight  # Tipos de luz
from panda3d.core import TransparencyAttrib  # Para lidar com transparência de texturas
from panda3d.core import WindowProperties  # Permite configurar a janela
from panda3d.core import ClockObject  # Controla o tempo no jogo
from panda3d.core import CollisionTraverser, CollisionNode  # Sistema de detecção de colisões
from panda3d.core import CollisionBox, CollisionRay, CollisionHandlerQueue

# Carrega configurações da engine a partir do arquivo settings.prc
loadPrcFile('settings.prc')

# Objeto global de relógio do Panda3D
globalClock = ClockObject.getGlobalClock()

# Função auxiliar para converter graus em radianos
def degToRad(degrees):
    return degrees * (pi / 180.0)

# Classe principal do jogo, herdando da ShowBase do Panda3D
class Minecraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Toca música de fundo
        self.play_music("theme.ogg")

        # Bloco selecionado inicialmente
        self.selectedBlockType = 'sand'

        # Carrega todos os modelos, luzes, terreno etc.
        self.loadModels()
        self.setupLights()
        self.generateTerrain()
        self.setupCamera()
        self.setupSkybox()
        self.captureMouse()
        self.setupControls()

        # Adiciona uma tarefa de atualização chamada 'update' para rodar a cada frame
        self.taskMgr.add(self.update, 'update')
    
    # Função chamada a cada frame
    def update(self, task):
        dt = globalClock.getDt()  # Tempo decorrido desde o último frame

        playerMoveSpeed = 10  # Velocidade do jogador
        x_movement = 0
        y_movement = 0
        z_movement = 0

        # Controles de movimento baseados nas teclas pressionadas
        if self.keyMap['forward']:
            x_movement -= dt * playerMoveSpeed * sin(degToRad(self.camera.getH()))
            y_movement += dt * playerMoveSpeed * cos(degToRad(self.camera.getH()))
        if self.keyMap['backward']:
            x_movement += dt * playerMoveSpeed * sin(degToRad(self.camera.getH()))
            y_movement -= dt * playerMoveSpeed * cos(degToRad(self.camera.getH()))
        if self.keyMap['left']:
            x_movement -= dt * playerMoveSpeed * cos(degToRad(self.camera.getH()))
            y_movement -= dt * playerMoveSpeed * sin(degToRad(self.camera.getH()))
        if self.keyMap['right']:
            x_movement += dt * playerMoveSpeed * cos(degToRad(self.camera.getH()))
            y_movement += dt * playerMoveSpeed * sin(degToRad(self.camera.getH()))
        if self.keyMap['up']:
            z_movement += dt * playerMoveSpeed
        if self.keyMap['down']:
            z_movement -= dt * playerMoveSpeed
        
        # Atualiza a posição da câmera (jogador)
        self.camera.setPos(
            self.camera.getX() + x_movement,
            self.camera.getY() + y_movement,
            self.camera.getZ() + z_movement,
        )

        # Controle da rotação da câmera com o movimento do mouse
        if self.cameraSwingActivated:
            md = self.win.getPointer(0)
            mouseX = md.getX()
            mouseY = md.getY()

            mouseChangeX = mouseX - self.lastMouseX
            mouseChangeY = mouseY - self.lastMouseY

            self.cameraSwingFactor = 40  # Sensibilidade do giro da câmera com o mouse

            currentH = self.camera.getH()
            currentP = self.camera.getP()

            # Altera a orientação da câmera (cabeça do jogador)
            self.camera.setHpr(
                currentH - mouseChangeX * dt * self.cameraSwingFactor,
                min(90, max(-90, currentP - mouseChangeY * dt * self.cameraSwingFactor)),
                0
            )

            # Atualiza o último valor do mouse
            self.lastMouseX = mouseX
            self.lastMouseY = mouseY

        return task.cont  # Continua executando a tarefa
    
    # Atualiza o dicionário de teclas pressionadas
    def updateKeyMap(self, key, value):
        self.keyMap[key] = value
    
    # Altera o tipo de bloco selecionado
    def SelectedBlockType(self, type):
        self.selectedBlockType = type
    
    # Ativa o modo de captura do mouse (oculta o cursor e trava dentro da janela)
    def captureMouse(self):
        self.cameraSwingActivated = True

        md = self.win.getPointer(0)
        self.lastMouseX = md.getX()
        self.lastMouseY = md.getY()

        properties = WindowProperties()
        properties.setCursorHidden(True)
        properties.setMouseMode(WindowProperties.M_relative)
        self.win.requestProperties(properties)
    
    # Libera o mouse (torna visível e destrava da janela)
    def releaseMouse(self):
        self.cameraSwingActivated = False

        properties = WindowProperties()
        properties.setCursorHidden(False)
        properties.setMouseMode(WindowProperties.M_absolute)
        self.win.requestProperties(properties)
    
    # Clique esquerdo: captura mouse e remove bloco sob mira
    def leftClick(self):
        self.captureMouse()
        self.removeBlock()
    
    # Carrega os modelos dos blocos
    def loadModels(self):
        self.dirtBlock = self.loader.loadModel('dirt-block.glb')
        self.stoneBlock = self.loader.loadModel('stone-block.glb')
        self.sandBlock = self.loader.loadModel('sand-block.glb')
    
    # Remove um bloco com base na detecção de colisão do raio
    def removeBlock(self):
        if self.rayQueue.getNumEntries() > 0:
            self.rayQueue.sortEntries()
            rayHit = self.rayQueue.getEntry(0)

            hitNodePath = rayHit.getIntoNodePath()
            hitObject = hitNodePath.getPythonTag('owner')
            distanceFromPlayer = hitObject.getDistance(self.camera)

            if distanceFromPlayer < 12:
                hitNodePath.clearPythonTag('owner')
                hitObject.removeNode()
                self.play_sound("remove_block.ogg") 
    
    # Cria um novo bloco na posição indicada
    def createNewBlock(self, x, y, z, type):
        newBlockNode = self.render.attachNewNode('new-block-placeholder')
        newBlockNode.setPos(x, y, z)

        # Escolhe o tipo de bloco
        if type == 'dirt':
            self.dirtBlock.instanceTo(newBlockNode)
        elif type == 'sand':
            self.sandBlock.instanceTo(newBlockNode)
        elif type == 'stone':
            self.stoneBlock.instanceTo(newBlockNode)
        
        # Adiciona colisão ao bloco
        blockSolid = CollisionBox((-1, -1, -1), (1, 1, 1))
        blockNode = CollisionNode('block-collision-node')
        blockNode.addSolid(blockSolid)
        collider = newBlockNode.attachNewNode(blockNode)
        collider.setPythonTag('owner', newBlockNode)
    
    # Coloca um bloco na posição da mira
    def placeBlock(self):
        if self.rayQueue.getNumEntries() > 0:
            self.rayQueue.sortEntries()
            rayHit = self.rayQueue.getEntry(0)
            hitNodePath = rayHit.getIntoNodePath()
            normal = rayHit.getSurfaceNormal(hitNodePath)
            hitObject = hitNodePath.getPythonTag('owner')
            distanceFromPlayer = hitObject.getDistance(self.camera)

            if distanceFromPlayer < 14:
                hitBlockPos = hitObject.getPos()
                newBlockPos = hitBlockPos + normal * 2
                self.createNewBlock(newBlockPos.x, newBlockPos.y, newBlockPos.z, self.selectedBlockType)
                self.play_sound("create_block.ogg")
    
    # Configura os controles do teclado e mouse
    def setupControls(self):
        self.keyMap = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }

        # Controles especiais
        self.accept('escape', self.releaseMouse)
        self.accept('mouse1', self.leftClick)
        self.accept('mouse3', self.placeBlock)

        # Movimento com teclado (WASD + espaço/lshift)
        self.accept('w', self.updateKeyMap, ['forward', True])
        self.accept('w-up', self.updateKeyMap, ['forward', False])
        self.accept('a', self.updateKeyMap, ['left', True])
        self.accept('a-up', self.updateKeyMap, ['left', False])
        self.accept('s', self.updateKeyMap, ['backward', True])
        self.accept('s-up', self.updateKeyMap, ['backward', False])
        self.accept('d', self.updateKeyMap, ['right', True])
        self.accept('d-up', self.updateKeyMap, ['right', False])
        self.accept('space', self.updateKeyMap, ['up', True])
        self.accept('space-up', self.updateKeyMap, ['up', False])
        self.accept('lshift', self.updateKeyMap, ['down', True])
        self.accept('lshift-up', self.updateKeyMap, ['down', False])

        # Teclas para trocar o tipo de bloco
        self.accept('1', self.SelectedBlockType, ['dirt'])
        self.accept('2', self.SelectedBlockType, ['sand'])
        self.accept('3', self.SelectedBlockType, ['stone'])
    
    # Configura a câmera e a mira
    def setupCamera(self):
        self.disableMouse()  # Desativa controle padrão da câmera
        self.camera.setPos(0, 0, 3)  # Posição inicial
        self.camLens.setFov(80)  # Campo de visão

        # Adiciona uma imagem de mira ao centro da tela
        crosshairs = OnscreenImage(
            image = 'crosshairs.png',
            pos = (0, 0, 0),
            scale = 0.05,
        )
        crosshairs.setTransparency(TransparencyAttrib.MAlpha)

        # Sistema de detecção de colisão por raio para selecionar blocos
        self.cTrav = CollisionTraverser()
        ray = CollisionRay()
        ray.setFromLens(self.camNode, (0, 0))
        rayNode = CollisionNode('line-of-sight')
        rayNode.addSolid(ray)
        rayNodePath = self.camera.attachNewNode(rayNode)
        self.rayQueue = CollisionHandlerQueue()
        self.cTrav.addCollider(rayNodePath, self.rayQueue)
    
    # Carrega a skybox (céu ao redor do mundo)
    def setupSkybox(self):
        skybox = self.loader.loadModel('skybox/skybox.egg')
        skybox.setScale(500)
        skybox.setBin('background', 1)
        skybox.setDepthWrite(0)
        skybox.setLightOff()
        skybox.reparentTo(self.render)
    
    # Gera um terreno de blocos 3D
    def generateTerrain(self):
        for z in range(10):
            for y in range(20):
                for x in range(20):
                    self.createNewBlock(
                        x * 2 - 20,
                        y * 2 - 20,
                        -z * 2,
                        'sand' if z == 0 else 'dirt'
                    )
    
    # Configura as luzes do mundo
    def setupLights(self):
        mainLight = DirectionalLight('main light')
        mainLightNodePath = self.render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        self.render.setLight(mainLightNodePath)

        ambientLight = AmbientLight('ambient light')
        ambientLight.setColor((0.3, 0.3, 0.3, 1))
        ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNodePath)
    
    # Toca música de fundo
    def play_music(self, file_name, loop=True, volume=0.3):
        self.music = self.loader.loadMusic(file_name)
        self.music.setLoop(loop)
        self.music.setVolume(volume)
        self.music.play()
    
    # Toca efeitos sonoros (ex: quebrar bloco)
    def play_sound(self, file_name, volume=1.0):
        sound = self.loader.loadSfx(file_name)
        sound.setVolume(volume)
        sound.play()

# Instancia o jogo e inicia a execução
game = Minecraft()
game.run()
