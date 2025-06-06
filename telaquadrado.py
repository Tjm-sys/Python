from panda3d.core import loadPrcFileData, CardMaker
from panda3d.core import WindowProperties, NodePath
from direct.showbase.ShowBase import ShowBase
loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Minha Primeira Janela")
class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()
        cm = CardMaker("meu_quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1) #largura e altura do quadrado
        quadrado = NodePath(cm.generate())
        quadrado.setColor(1, 0, 0, 1) #cor (RGBA)
        quadrado.setPos(0, 0, 0)
        quadrado.reparentTo(self.render2d)
MyApp().run()