import spyral
import model

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/missionControlButton.png")
        self.pos = (WIDTH/2, HEIGHT*2/3)
        self.anchor = 'center'
        spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.pop()

class TutorialScreen(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = model.resources["tutorial_bg"]

        missionControlButton = drawButton(self.scene)
        spyral.event.register("system.quit", spyral.director.quit)

