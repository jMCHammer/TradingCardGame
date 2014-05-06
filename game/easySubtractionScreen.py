import spyral
import random
import model
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

answerNum = 0

class drawQuestion(spyral.Sprite):
    def __init__(self, Scene, font, string):
        spyral.Sprite.__init__(self,Scene)
        self.text = string
        self.f = spyral.Font(font, 100)
        self.image = self.f.render(self.text)

    def update(self, string):
        self.text = string
        self.image = self.f.render(self.text)

class drawCarry(spyral.Sprite):
    def __init__(self, Scene, text):
        spyral.Sprite.__init__(self,Scene)
        self.string = text
        self.f = spyral.Font("Extras/Comic_Book.ttf", 50)
        self.image = self.f.render(self.string)

    def update(self, string):
        self.text = string
        self.image = self.f.render(self.text)

class drawButton(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        self.pos = (WIDTH/2.6, HEIGHT*9/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            if self.scene.q.x > self.scene.q.y:
                key = self.scene.q.x - self.scene.q.y
            else:
                key = self.scene.q.y - self.scene.q.x
            if answerNum == int(key):
                print "you're right"
            else: 
                print "you're wrong :("

class Question:#initiate two random numbers to add
    def __init__(self):
        self.x = 0
        self.y = 0
        self.text = ""

        self.x = random.randint(1,500)
        self.y = random.randint(1,500)

###################DRAW UP AND DOWN BUTTONS#################################

class drawup1Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum + 100
            self.scene.update()

class drawup2Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum + 10
            self.scene.update()

class drawup3Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum + 1
            self.scene.update()

class drawdown1Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum-100
            self.scene.update()

class drawdown2Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum- 10
            self.scene.update()

class drawdown3Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answerNum
            answerNum = answerNum -1
            self.scene.update()

####################################################################################

class EasySubtractionScreen(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        self.q = Question()
    
        subtractionssign = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "-")
        subtractionssign.pos = (WIDTH - 300, 130)

        questionText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(self.q.x))
        questionText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(self.q.y))
        if self.q.x > self.q.y:
            if self.q.x < 10:
                questionText1.pos = (WIDTH-78, 30)
            if self.q.x < 100 and self.q.x > 10:
                questionText1.pos = (WIDTH-150, 30)
            if self.q.x >100:
                questionText1.pos = (WIDTH-208, 30)
            if self.q.y < 10:
                questionText2.pos = (WIDTH-78, 130)
            if self.q.y < 100 and self.q.y > 10:
                questionText2.pos = (WIDTH-150, 130)
            if self.q.y >100:
                questionText2.pos = (WIDTH-208, 130)
        else:
            if self.q.x < 10:
                questionText1.pos = (WIDTH-78, 130)
            if self.q.x < 100 and self.q.x > 10:
                questionText1.pos = (WIDTH-150, 130)
            if self.q.x >100:
                questionText1.pos = (WIDTH-208, 130)
            if self.q.y < 10:
                questionText2.pos = (WIDTH-78, 30)
            if self.q.y < 100 and self.q.y > 10:
                questionText2.pos = (WIDTH-150, 30)
            if self.q.y >100:
                questionText2.pos = (WIDTH-208, 30)

        answerNum = 0

        questionText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "___")
        questionText3.pos = (WIDTH-250,130)
        self.answer = drawQuestion(self, "Extras/Comic_Book.ttf", str(answerNum))
        self.answer.pos = (WIDTH-220, 350)

        continuebutton = drawButton(self.scene, "Extras/continue.png")
        continuebutton.pos = (WIDTH/2-100, HEIGHT-100)
        explainationText = drawCarry(self.scene, "Subtract the digits in columns")
        explainationText.pos = (0,0)
        explainationText2 = drawCarry(self.scene, "by clicking the down arrow the")
        explainationText2.pos = (0,50)
        explainationText3 = drawCarry(self.scene, "combined amount of both numbers")
        explainationText3.pos = (0,100)
        explainationText4 = drawCarry(self.scene, "in each column.")
        explainationText4.pos = (0,150)
        explainationText5 = drawCarry(self.scene, "Don't forget borrowing.")
        explainationText5.pos = (0,200)
        explainationText6 = drawCarry(self.scene, "Click continue")
        explainationText6.pos = (0,300)
        explainationText7 = drawCarry(self.scene, "when you have your answer.")
        explainationText7.pos = (0,350)

        explainationText8 = drawCarry(self.scene, "Hint: start with your answer being")
        explainationText8.pos = (0,550)
        explainationText9 = drawCarry(self.scene, "the higher number and subtract out")
        explainationText9.pos = (0,600)
        explainationText7 = drawCarry(self.scene, "the bottom number.")
        explainationText7.pos = (0,650)

        ##drawing all up and down buttons as sprites
        up1Button = drawup1Button(self.scene, "Extras/up.png")
        up1Button.pos = (WIDTH -240,305)
        up2Button = drawup2Button(self.scene, "Extras/up.png")
        up2Button.pos = (WIDTH-158, 305)
        up3Button = drawup3Button(self.scene, "Extras/up.png")
        up3Button.pos = (WIDTH-80, 305)
        down1Button = drawdown1Button(self.scene, "Extras/down.png")
        down1Button.pos = (WIDTH-240, 505)
        down2Button = drawdown2Button(self.scene, "Extras/down.png")	
        down2Button.pos = (WIDTH-158, 505)
        down3Button = drawdown3Button(self.scene, "Extras/down.png")	
        down3Button.pos = (WIDTH-80, 505)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)

    def update(self):
        self.answer.update(str(answerNum))
