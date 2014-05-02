import spyral
import random
import model
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

answer1 = 0
answer2 = 0
answer3 = 0
answerNumber = 0

class drawQuestion(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 100)
        self.image = f.render(text)

class Question:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.text = ""

        self.x = random.randint(1,99)
        self.y = random.randint(1,99)

    def checkAnswer(self, key):
        if ops["+"](self.x, self.y) == key:
            return true
        
        else:
            return False

class drawButton(spyral.Sprite):
    def __init__(self, Scene, image, answerNumber):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        self.pos = (WIDTH/2.6, HEIGHT*9/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNumber
            answerNumber = answerNumber+1

class AdditionScreen(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")

        self.q = Question()

        questionText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", " " + str(self.q.x))
        if (self.q.x < 10):
            questionText1.pos = (WIDTH/2 + 72,0)
        else:
            questionText1.pos = (WIDTH/2,0)
        questionText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "+" + str(self.q.y))
        if (self.q.y < 10):
            questionText2.pos = (WIDTH/2 + 72,100)
        else:
            questionText2.pos = (WIDTH/2,100)
        questionText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "___")
        questionText3.pos = (WIDTH/2,100)
        answerText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer1))
        answerText1.pos = (WIDTH/2-20,350)
        answerText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer2))
        answerText2.pos = (WIDTH/2+52,350)
        answerText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer3))
        answerText3.pos = (WIDTH/2+124,350)

        up1Button = drawButton(self.scene, "Extras/up.png", answer1)
        up1Button.pos = (WIDTH/2 + 124,300)
        up2Button = drawButton(self.scene, "Extras/up.png", answer2)
        up2Button.pos = (WIDTH/2 + 52, 300)
        up3Button = drawButton(self.scene, "Extras/up.png", answer3)
        up3Button.pos = (WIDTH/2 - 20, 300)
        down1Button = drawButton(self.scene, "Extras/down.png", answer1)
        down1Button.pos = (WIDTH/2 + 52, 500)
        down2Button = drawButton(self.scene, "Extras/down.png", answer2)	
        down2Button.pos = (WIDTH/2 + 124, 500)
        down3Button = drawButton(self.scene, "Extras/down.png", answer3)	
        down3Button.pos = (WIDTH/2 -20, 500)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)

    def update():
        answerText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer1))
