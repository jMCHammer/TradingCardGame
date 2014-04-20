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

class drawImage(spyral.Sprite):
    def __init__(self, Scene, imageLoc, posx, posy):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(imageLoc)
        self.pos = (posx, posy)

class BeginFaceoffScreen(spyral.Scene):
    def __init__(self, hero):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = hero
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        hero.draw(self.scene)
        hero.pos = (WIDTH*4/5, 400) 

        vsImage = drawImage(self.scene, "Extras/vs.png", WIDTH/3, 225)
        opponentImage = drawImage(self.scene, "Extras/girl.png", WIDTH/13, 50)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
