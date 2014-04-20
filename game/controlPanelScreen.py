import spyral
import random
import math
import editCollectionScreen
import beginFaceoffScreen

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

class drawFaceoffButton(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/faceoff.png")
	    self.pos = (WIDTH/4.5, 300)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            faceoff = beginFaceoffScreen.BeginFaceoffScreen(hero)
            spyral.director.push(faceoff)

class ControlPanelScreen(spyral.Scene):
    def __init__(self, heroInstance):
        global manager
        global hero
        spyral.Scene.__init__(self, SIZE)
        hero = heroInstance
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        charText = drawFont(self.scene, "Extras/Comic_Book.ttf", "Welcome " + hero.name + "!")
        charText.pos = (WIDTH/3, 10)

        hero.draw(self.scene)
        hero.pos = (WIDTH*3/4, 200) 

        faceoffButton = drawFaceoffButton(self.scene)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
