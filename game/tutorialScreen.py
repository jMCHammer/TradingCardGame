import spyral
import model

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class TutorialScreen(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = model.resources["tutorial_bg"]

        class RegisterForm(spyral.Form):
            #Buttons
            backButton   = spyral.widgets.Button("Mission Control")
        self.form = RegisterForm(self)
        self.form.backButton.pos   = (WIDTH/2- 40, HEIGHT*2/3)

        spyral.event.register("form.RegisterForm.backButton.changed", self.backClicked)
        spyral.event.register("system.quit", spyral.director.quit)

################### Exit ##################################################
#### Go back to controlPanelScreen
    def backClicked(self, event):
        if (event.value == "down"):
            spyral.director.pop()
