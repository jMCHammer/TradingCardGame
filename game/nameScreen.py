import spyral
import random
import math
import model
import controlPanelScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawTitleFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 150, WHITE)
        self.image = f.render(text)

class drawTextFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
	    spyral.Sprite.__init__(self, Scene)
	    f = spyral.Font(font, 50, WHITE)
	    self.image = f.render(text)

class drawCharOneImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char1.png")
	    self.pos = (WIDTH/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char1"
            print model.char

class drawCharTwoImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char2.png")
	    self.pos = (WIDTH*2/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char2"
            print model.char

class drawCharThreeImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char3.png")
	    self.pos = (WIDTH*3/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char3"
            print model.char

class drawCharFourImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char4.png")
	    self.pos = (WIDTH*4/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char4"
            print model.char

class drawCharFiveImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char5.png")
	    self.pos = (WIDTH*5/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char5"
            print model.char

class drawCharSixImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/char6.png")
	    self.pos = (WIDTH*6/8, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.char = "char6"
            print model.char

class drawButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/continueButton.png")
        self.pos = (WIDTH/2.4, HEIGHT*9.5/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.name = self.scene.form.nameAnswer.value
            model.opponentDead = False
            cps = controlPanelScreen.ControlPanelScreen()
            spyral.director.replace(cps)

class NameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = model.resources["background"]

        startText = drawTitleFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        charText = drawTextFont(self.scene, "Extras/Comic_Book.ttf", "CLICK YOUR CHARACTER")
        charText.pos = (WIDTH/5, 200)

        self.char1Image = drawCharOneImage(self.scene)
        self.char2Image = drawCharTwoImage(self.scene)	
        self.char3Image = drawCharThreeImage(self.scene)
        self.char4Image = drawCharFourImage(self.scene)
        self.char5Image = drawCharFiveImage(self.scene)
        self.char6Image = drawCharSixImage(self.scene)

        class RegisterForm(spyral.Form):
            nameAnswer = spyral.widgets.TextInput(275, "Enter your name here.")

        self.form = RegisterForm(self)
        self.form.nameAnswer.pos = (WIDTH/2.75, HEIGHT*9/10)

        continueButton = drawButton(self.scene)		

        spyral.event.register("system.quit", spyral.director.pop)

