import spyral
import random
import math

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

class drawVsImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/vs.png")

class drawOpponentImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/girl.png")

class BeginFaceoffScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

	    characterImage = drawCharacterImage(self.scene)
	    characterImage.pos = (WIDTH*4/5, 400)

	    vsImage = drawVsImage(self.scene)
	    vsImage.pos = (WIDTH/3, 225)

	    opponentImage = drawOpponentImage(self.scene)
	    opponentImage.pos = (WIDTH/13,50)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
