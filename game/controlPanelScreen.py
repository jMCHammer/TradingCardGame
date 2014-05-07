import spyral
import model
import editCollectionScreen
import beginFaceoffScreen

from hero import Hero

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 50, WHITE)
        self.image = f.render(text)

class drawFaceoffButton(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/faceoffButton.png")
	    self.pos = (WIDTH/4, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            faceoff = beginFaceoffScreen.BeginFaceoffScreen()
            spyral.director.push(faceoff)

class drawEditDeckButton(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/editDeckButton.png")
	    self.pos = (WIDTH/4, 400)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            edit = editCollectionScreen.EditCollectionScreen()
            spyral.director.push(edit)

class drawTutorialButton(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/tutorialButton.png")
	    self.pos = (WIDTH/4, 500)

class drawCodeButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/saveGameCodeButton.png")
        self.pos = (WIDTH/4, 600)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        #if button already clicked
        try:
            self.codeText.visible = False
#            del self.codeText
        except:
            pass        
        if self.collide_point(pos):
            sc = "Game Code: " + model.saveCode()
            self.codeText = drawFont(self.scene, "Extras/Comic_Book.ttf", sc)
            self.codeText.pos = (WIDTH/2 - 100, HEIGHT*4/5)


class ControlPanelScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self.scene)
        self.background = model.resources["background"]

        charText = drawFont(self.scene, "Extras/Comic_Book.ttf", "Welcome " + self.hero.name + "!")
        charText.pos = (WIDTH/3, 10)

        self.hero.pos = (WIDTH*2.5/4, 200) 

        faceoffButton = drawFaceoffButton(self.scene)
        editDeckButton = drawEditDeckButton(self.scene)
        tutorialButton = drawTutorialButton(self.scene)
        showGameCodeButton = drawCodeButton(self.scene)

        spyral.event.register("system.quit", spyral.director.pop)

