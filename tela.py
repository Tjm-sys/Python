from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Minha Primeira Janela")
class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()
MyApp().run()