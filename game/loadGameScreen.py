import spyral
import controlPanelScreen
import model

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text, size):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, size, WHITE)
        self.image = f.render(text)

class LoadGameScreen(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = model.resources["background"]

        class RegisterForm(spyral.Form):
            #Fields
            answerField  = spyral.widgets.TextInput(50, "")
            submitButton   = spyral.widgets.Button("Submit")

        self.form = RegisterForm(self)
        self.form.answerField.pos = (WIDTH/2 + 80, HEIGHT*3/4 + 20)
        self.form.submitButton.pos = (WIDTH/2 + 160, HEIGHT*3/4 + 20)

        title = drawFont(self.scene, "Extras/Comic_Book.ttf", "Enter in your game code", 40)
        title.pos = (120, HEIGHT*3/4) 
        spyral.event.register("system.quit", spyral.director.quit)
        spyral.event.register("form.RegisterForm.submitButton.changed", self.submit)

    def submit(self, event):
        if (event.value == "down"):
            if self.form.answerField.value:
                if model.loadCode(self.form.answerField.value):
                    spyral.director.replace(controlPanelScreen.ControlPanelScreen())
                else:
                    wrongText = drawFont(self.scene, "Extras/Comic_Book.ttf", "Invalid Code, try again", 40)
                    wrongText.pos = (WIDTH/3 - 40, HEIGHT/2 + 80)
