import spyral
import faceoffScreen
import model

from opponent import Opponent
from hero import Hero

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

class drawBattleButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        #TODO: Create "Battle!" button
        self.image = spyral.image.Image("Extras/faceoff.png")
        self.pos = (WIDTH/4.5, 300)
        spyral.event.register("input.mouse.down.left", self.handle_clicked) 

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class BeginFaceoffScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self.scene)
        self.background = model.resources["background"]

        self.hero.pos = (WIDTH*4/5, 400) 

        drawBattleButton(self)
        drawImage(self.scene, "Extras/vs.png", WIDTH/3, 225)
        opp = Opponent(self, "Youngster Joey")
        opp.pos = (WIDTH/13, 50)
      #  drawImage(self.scene, "Extras/Youngster_.png", WIDTH/13, 50)

        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
