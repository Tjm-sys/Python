from math import pi, sin ,cos
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile, DirectionalLight, AmbientLight
from panda3d.core import WindowProperties, ClockObject, GeomNode, CardMaker
from panda3d.core import Texture, LVector3, Vec4

#cria um local na memória para rodar
loadPrcFile('settings.prc')
globalClock = ClockObject.getGlobalClock()

#calculo de graus para radiando
def degToRad(degrees):
    return degrees * (pi / 180.0)

class Minecraft(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #configurando janela
        self.disable_mouse
        props = WindowProperties
        props.setCursorHidden(True)
        self.win.requestPropities(props)

        #inicializa os controles do teclado
        self.keyMap = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        #atualiza o mapa de comandos quando se é pressionado uma tecla
        self.accept("w", self.updateKeyMap, ["forward", True])
        self.accept("w-up", self.updateKeyMap, ["forward", False])
        self.accept("s", self.updateKeyMap, ["backward", True])
        self.accept("s-up", self.updateKeyMap, ["backward", False])
        self.accept("a", self.updateKeyMap, ["backward", True])
        self.accept("a-up", self.updateKeyMap, ["backward", False])
        self.accept("d", self.updateKeyMap, ["backward", True])
        self.accept("d-up", self.updateKeyMap, ["backward", False])
        self.accept("space", self.updateKeyMap, ["backward", True])
        self.accept("space-up", self.updateKeyMap, ["backward", False])
        self.accept("shift", self.updateKeyMap, ["backward", True])
        self.accept("shift-up", self.updateKeyMap, ["backward", False])
        self.accept("escape", self.quit)

        #configuração da câmera
        self.camera.setPos(0, -10, 2)
        self.cameraSwinActivated = True
        self.lastMouseX = self.win.getPointer(0).getX()
        self.lastMouseY = self.win.getPointer(0).getY()

        def update(self, task):
            dt = globalClock.getDt()

            #movimentação do player

        #Coltrole da câmera com o mouse
            if self.cameraSwinActivated:
                md = self.win.getPointer(0)
                mouseX = md.getX()
                mouseY = md.getY()

                mouseChangeX = mouseX - self.lastMouseX
                mouseChangeY = mouseY - self.lastMouseY

                self.cameraSwinFactor = 50

                currentH = self.camera.getH()
                currentP = self.camera.getP()

                self.camera.setHpr(
                currentH - mouseChangeX * dt * self.cameraSwingFactor,
                min(90, max(-90, currentP - mouseChangeY * dt * self.cameraSwinFactor)), 0)
            
                self,lastMouseX = mouseX
                self,lastMouseY = mouseY

            return task.cont