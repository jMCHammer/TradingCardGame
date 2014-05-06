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

class drawQuestion(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        self.string = text
        self.f = spyral.Font(font, 100)
        self.image = self.f.render(self.string)

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
            guess = str(answer1) + str(answer2) + str(answer3)
            key = self.scene.q.x + self.scene.q.y
            if int(guess) == int(key):
                print "you're right"
            else: 
                print "you're wrong :("

class Question:#initiate two random numbers to add
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

###################DRAW UP AND DOWN BUTTONS#################################

class drawup1Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        self.pos = (WIDTH/2.6, HEIGHT*9/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer1
            answer1 = answer1 +1
            self.scene.update()

class drawup2Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer2
            answer2 = answer2 +1
            if answer2 == 10:
                answer2 = 0
                self.scene.carry2()
            self.scene.update()

class drawup3Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer3
            answer3 = answer3 +1
            if answer3 == 10:
                answer3 = 0
                self.scene.carry1()
            self.scene.update()

class drawdown1Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer1
            if answer1 >0 :
                answer1 = answer1 -1
            self.scene.update()

class drawdown2Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer2
            if answer2 > 0:
                answer2 = answer2 -1
            self.scene.update()

class drawdown3Button(spyral.Sprite):
    def __init__(self, Scene, image):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(image)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            global answer3
            if answer3 > 0:
                answer3 = answer3 -1
            self.scene.update()

####################################################################################

class EasyAdditionScreen(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        self.q = Question()

        #draw all question numbers as well as starting "000" answer
        questionText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", " " + str(self.q.x))
        if (self.q.x < 10):
            questionText1.pos = (WIDTH -158,30)
        else:
            questionText1.pos = (WIDTH-230,30)
        questionText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "+" + str(self.q.y))
        if (self.q.y < 10):
            questionText2.pos = (WIDTH -168,130)
        else:
            questionText2.pos = (WIDTH-235,130)
        questionText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "___")
        questionText3.pos = (WIDTH-250,130)
        self.answerText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer1))
        self.answerText1.pos = (WIDTH-280,380)
        self.answerText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer2))
        self.answerText2.pos = (WIDTH-198,380)
        self.answerText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(answer3))
        self.answerText3.pos = (WIDTH-120,380)

        continuebutton = drawButton(self.scene, "Extras/continue.png")
        continuebutton.pos = (WIDTH/2-100, HEIGHT-100)
        explainationText = drawCarry(self.scene, "Add the digits in columns")
        explainationText.pos = (0,0)
        explainationText2 = drawCarry(self.scene, "by clicking the up arrow the")
        explainationText2.pos = (0,50)
        explainationText3 = drawCarry(self.scene, "combined amount of both numbers")
        explainationText3.pos = (0,100)
        explainationText4 = drawCarry(self.scene, "in each column.")
        explainationText4.pos = (0,150)
        explainationText5 = drawCarry(self.scene, "Don't forget to carry the 1s.")
        explainationText5.pos = (0,200)
        explainationText6 = drawCarry(self.scene, "Click continue")
        explainationText6.pos = (0,300)
        explainationText7 = drawCarry(self.scene, "when you have your answer.")
        explainationText7.pos = (0,350)

        ##drawing all up and down buttons as sprites
        up1Button = drawup1Button(self.scene, "Extras/up.png")
        up1Button.pos = (WIDTH -270,330)
        up2Button = drawup2Button(self.scene, "Extras/up.png")
        up2Button.pos = (WIDTH-188, 330)
        up3Button = drawup3Button(self.scene, "Extras/up.png")
        up3Button.pos = (WIDTH-110, 330)
        down1Button = drawdown1Button(self.scene, "Extras/down.png")
        down1Button.pos = (WIDTH-270, 530)
        down2Button = drawdown2Button(self.scene, "Extras/down.png")	
        down2Button.pos = (WIDTH-188, 530)
        down3Button = drawdown3Button(self.scene, "Extras/down.png")	
        down3Button.pos = (WIDTH-110, 530)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)

    def carry1(self):#drawing carry to 10's
        self.carrytext1 = drawCarry(self.scene, "1")
        self.carrytext1.pos = (WIDTH/2 + 72,0)

    def carry2(self):#draw carry to 100's
        self.carrytext2 = drawCarry(self.scene, "1")
        self.carrytext2.pos = (WIDTH/2 +30,0)

    def update(self): #updates values and redraws so they don't overlap
        self.answerText1.update(str(answer1))
        self.answerText2.update(str(answer2))
        self.answerText3.update(str(answer3))
