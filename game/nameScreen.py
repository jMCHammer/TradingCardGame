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
GENDER = ""


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

class drawButton(spyral.Sprite):
    def __init__(self, Scene, imageloc, posx, posy):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(imageloc)
        self.pos = (posx, posy)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)    

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.replace(controlPanelScreen.ControlPanelScreen(Hero(self.name, GENDER)))  

class drawBoyImage(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/boy.png")
        self.pos = (WIDTH/5, 300)
        self.gender = ""
        spyral.event.register("input.mouse.down.left", self.handle_clicked)    

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global GENDER 
            GENDER = "boy"

class drawGirlImage(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/girl.png")
        self.pos = (WIDTH*3/5, 300)
        self.gender = ""
        spyral.event.register("input.mouse.down.left", self.handle_clicked)    

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global GENDER
            GENDER = "girl"

class NameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        startText = drawTitleFont(self.scene, "Extras/Comic_Book.ttf", "FACEOFF")
        startText.pos = (WIDTH/4, 10)

        charText = drawTextFont(self.scene, "Extras/Comic_Book.ttf", "CHOOSE YOUR CHARACTER")
        charText.pos = (WIDTH/5, 200)

        self.boyImage = drawBoyImage(self.scene)
        self.girlImage = drawGirlImage(self.scene)    
        continueButton = drawButton(self, "Extras/continue.png", WIDTH/2.6, HEIGHT*9/10)            

        class RegisterForm(spyral.Form):
            #nameButton = spyral.widgets.Button("Continue")
            nameAnswer = spyral.widgets.TextInput(275, "Enter your name here.")

        form = RegisterForm(self)
        #form.nameButton.pos = (WIDTH/2.25, HEIGHT*9/10)
        form.nameAnswer.pos = (WIDTH/2.75, HEIGHT*8.5/10)

        def continueClick(event):
            if (event.value == "down"):
                self.name = form.nameAnswer.value
                cps = controlPanelScreen.ControlPanelScreen(Hero(self.name, GENDER))
                spyral.director.replace(cps)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        #spyral.event.register("form.RegisterForm.nameButton.changed", continueClick)
