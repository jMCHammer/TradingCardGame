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

class drawOpponentOneImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent1.png")
	    self.pos = (WIDTH/8, 200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent1"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class drawOpponentTwoImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent2.png")
	    self.pos = (WIDTH*3/8, 200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent2"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class drawOpponentThreeImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent3.png")
	    self.pos = (WIDTH*5/8, 200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent3"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class drawOpponentFourImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent4.png")
	    self.pos = (WIDTH*2/8, 400)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent4"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class drawOpponentFiveImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent5.png")
	    self.pos = (WIDTH*4/8, 400)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent5"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class drawOpponentSixImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.image = spyral.image.Image("Extras/opponent6.png")
	    self.pos = (WIDTH*6/8, 400)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.currentOpponent = "opponent6"
            spyral.director.replace(faceoffScreen.FaceoffScreen())

class BeginFaceoffScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self.scene)
        self.background = model.resources["background"]

        self.hero.visible = False;
    
        opponentText = drawFont(self.scene, "Extras/Comic_Book.ttf", "Choose Your Opponent")
        opponentText.pos = (WIDTH/5, 10)

        self.opponent1Image = drawOpponentOneImage(self.scene);
        self.opponent2Image = drawOpponentTwoImage(self.scene);
        self.opponent3Image = drawOpponentThreeImage(self.scene);
        self.opponent4Image = drawOpponentFourImage(self.scene);
        self.opponent5Image = drawOpponentFiveImage(self.scene);
        self.opponent6Image = drawOpponentSixImage(self.scene);
        

        spyral.event.register("system.quit", spyral.director.quit)

