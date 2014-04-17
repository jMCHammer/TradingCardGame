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

class StartScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        
        startText = drawFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        class RegisterForm(spyral.Form):
            startButton = spyral.widgets.Button("START GAME")

        form = RegisterForm(self)
        form.startButton.pos = (WIDTH/2.25, HEIGHT*4/5)

        def startClick(event):
            if (event.value == "down"):
                spyral.director.replace(nameScreen.NameScreen())
	

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register("form.RegisterForm.startButton.changed", startClick)


