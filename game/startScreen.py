import spyral
import nameScreen
import loadGameScreen
import model

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 150, WHITE)
        self.image = f.render(text)

class drawButton(spyral.Sprite):
    def __init__(self, Scene, imageloc, posx, posy, name):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(imageloc)
        self.pos = (posx, posy)
        self.name = name
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            if self.name == "start":
                spyral.director.replace(nameScreen.NameScreen())            
            elif self.name == "loadgame":
                spyral.director.replace(loadGameScreen.LoadGameScreen())            
            
class StartScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        model.loadResources()
        self.background = model.resources["background"]
        
        startText = drawFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        drawButton(self, "Extras/startgame.png", WIDTH/2.5, HEIGHT*3/5, "start")
        drawButton(self, "Extras/startgame.png", WIDTH/2.5, HEIGHT*4/5, "loadgame")

        spyral.event.register("system.quit", spyral.director.pop)


