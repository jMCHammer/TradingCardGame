import spyral
import random
import math
import editCollectionScreen

#import beginFaceOffScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 50)
        self.image = f.render(text) 

class drawCharacterImage(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/boy.png")
        self.clicked = False    

class drawButton(spyral.Sprite):
    def __init__(self, Scene, imageloc, posx, posy):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image(imageloc)
	    self.pos = (posx, posy)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
	    spyral.director.replace(controlPanelScreen.ControlPanelScreen(Hero(self.name, GENDER)))  

class ControlPanelScreen(spyral.Scene):
    def __init__(self, hero):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = hero;
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        charText = drawFont(self.scene, "Extras/Comic_Book.ttf", "Welcome " + self.hero.name + "!")
        charText.pos = (WIDTH/3, 10)

        characterImage = drawCharacterImage(self.scene)
        characterImage.pos = (WIDTH*3/4, 200)

	faceoffButton = drawButton(self, "Extras/faceoff.png", WIDTH/4, 300)
	editdeckButton = drawButton(self, "Extras/editdeck.png", WIDTH/4, 300)
	tutorialButton = drawButton(self, "Extras/tutorial.png", WIDTH/4, 300)

        #class RegisterForm(spyral.Form):
        #    faceoffButton = spyral.widgets.Button("FACEOFF!")
        #    editDeckButton = spyral.widgets.Button("EDIT DECK!")
        #    tutorialButton = spyral.widgets.Button("TUTORIAL!")

        #form = RegisterForm(self)
        #form.faceoffButton.pos = (WIDTH/4, 300)
        #form.editDeckButton.pos = (WIDTH/4, 400)
        #form.tutorialButton.pos = (WIDTH/4, 500)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
#        spyral.event.register("form.RegisterForm.faceoffButton.changed", )
#        spyral.event.register("form.RegisterForm.tutorialButton.changed", )
        spyral.event.register("form.RegisterForm.editDeckButton.changed", self.editDeck)

    def editDeck(self, event):
        if (event.value == "down"):
            spyral.director.push(editCollectionScreen.EditCollectionScreen(self.hero))
            return

