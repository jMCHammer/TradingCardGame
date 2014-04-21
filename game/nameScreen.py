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
        f = spyral.Font(font, 150)
        self.image = f.render(text)

class drawTextFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
	    spyral.Sprite.__init__(self, Scene)
	    f = spyral.Font(font, 50)
	    self.image = f.render(text)

class drawBoyImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/boy.png")
	    self.pos = (WIDTH/5, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.gender = "boy"

class drawGirlImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/girl.png")
	    self.pos = (WIDTH*3/5, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.gender = "girl"

class drawButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/continue.png")
        self.pos = (WIDTH/2.6, HEIGHT*9/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.name = self.scene.form.nameAnswer.value
            cps = controlPanelScreen.ControlPanelScreen()
            spyral.director.replace(cps)

class NameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        startText = drawTitleFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        charText = drawTextFont(self.scene, "Extras/Comic_Book.ttf", "CLICK YOUR CHARACTER")
        charText.pos = (WIDTH/5, 200)

        self.boyImage = drawBoyImage(self.scene)
        self.girlImage = drawGirlImage(self.scene)	

        class RegisterForm(spyral.Form):
            nameAnswer = spyral.widgets.TextInput(275, "Enter your name here.")

        self.form = RegisterForm(self)
        self.form.nameAnswer.pos = (WIDTH/2.75, HEIGHT*8.5/10)

        continueButton = drawButton(self.scene)		

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
