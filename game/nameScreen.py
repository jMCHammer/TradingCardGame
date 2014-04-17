import spyral
import random
import math
import controlPanelScreen
from hero import Hero

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
	self.clicked = False	

    def setImage(self, pos):
	if (not self.clicked and self.inRange(pos)):
	    self.clicked = True
	
    def inRange(self, pos):
	r = self.rect
	return ((pos[0] > r.left and pos[0] < r.right) and 
		(pos[1] > r.top and pos[1] < r.bottom)) 		

class drawGirlImage(spyral.Sprite):
    def __init__(self, Scene):
	spyral.Sprite.__init__(self, Scene)
	self.image = spyral.image.Image("Extras/girl.png")
	self.clicked = False	

    def setImage(self, pos):
	if (not self.clicked and self.inRange(pos)):
	    self.clicked = True

    def inRange(self, pos):
        r = self.rect
        return ((pos[0] > r.left and pos[0] < r.right) and 
	        (pos[1] > r.top and pos[1] < r.bottom))		


class NameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        scen = spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("game/rsz_tundraclimate.png")

	startText = drawTitleFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
	startText.pos = (WIDTH/4, 10)

	charText = drawTextFont(self.scene, "Extras/Comic_Book.ttf", "CHOOSE YOUR CHARACTER")
	charText.pos = (WIDTH/5, 200)

	boyImage = drawBoyImage(self.scene)		
	boyImage.pos = (WIDTH/5, 300)		

	girlImage = drawGirlImage(self.scene)		
	girlImage.pos = (WIDTH*3/5, 300)

	if (boyImage.clicked):
	    gender = "boy"	
	elif (girlImage.clicked):
	    gender = "girl"
	else:
	    gender = "trans"		
	

	class RegisterForm(spyral.Form):
            nameButton = spyral.widgets.Button("Continue")
            nameAnswer = spyral.widgets.TextInput(275, "Enter your name here.")

        form = RegisterForm(self)
	form.nameButton.pos = (WIDTH/2.25, HEIGHT*9/10)
        form.nameAnswer.pos = (WIDTH/2.75, HEIGHT*8.5/10)

	def continueClick(event):
	    if (event.value == "down"):
		self.name = form.nameAnswer.value
		cps = controlPanelScreen.ControlPanelScreen(Hero(self.name))
		spyral.director.replace(cps)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
	spyral.event.register("form.RegisterForm.nameButton.changed", continueClick)
