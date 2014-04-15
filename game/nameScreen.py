import spyral
import random
import math
import genderScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 150)
        self.image = f.render(text)

class NameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("game/rsz_tundraclimate.png")
	startText = drawFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
	startText.pos = (WIDTH/4,HEIGHT/5)

	class RegisterForm(spyral.Form):
            nameButton = spyral.widgets.Button("Continue")
            nameAnswer = spyral.widgets.TextInput(275, "Enter your name here.")

        form = RegisterForm(self)
	form.nameButton.pos = (WIDTH/2.25, HEIGHT*4/5)
        form.nameAnswer.pos = (WIDTH/2.75, HEIGHT*3.5/5)

        name = form.nameAnswer.value

	def continueClick(event):
	    if (event.value == "down"):
		spyral.director.replace(genderScreen.GenderScreen())

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	spyral.event.register("form.RegisterForm.nameButton.changed", continueClick)

