import spyral
import random
import math
import nameScreen

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

class drawButton(spyral.Sprite):
    def __init__(self, Scene, imageloc, posx, posy):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image(imageloc)
	    self.pos = (posx, posy)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
	        spyral.director.replace(nameScreen.NameScreen())            

class StartScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        
        startText = drawFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        startButton = drawButton(self, "Extras/startgame.png", WIDTH/2.25, HEIGHT*4/5)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)

