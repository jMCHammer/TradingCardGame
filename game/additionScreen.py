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
            key = self.scene.q.x + self.scene.q.y
            if int(key) == int(self.scene.answer.text):
                print "you're right"
            else: 
                print "you're wrong :("

class Question:#initiate two random numbers to add
    def __init__(self, difficulty):
        self.x = 0
        self.y = 0
        self.text = ""
        self.level = difficulty

        if self.level == "Hard":
            self.x = random.randint(1,1000)
            self.y = random.randint(1,1000)
        else:
            self.x = random.randint(1,99)
            self.y = random.randint(1,99)

class AdditionScreen(spyral.Scene):
    def __init__(self, difficulty):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.image.Image("Extras/rsz_tundraclimate.png")
        self.q = Question(difficulty)
    
        subtractionssign = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "+")
        subtractionssign.pos = (WIDTH - 300, 130)

        #draw all question numbers as well as starting "000" answer

        questionText1 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(self.q.x))
        questionText2 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", str(self.q.y))
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
        
        questionText3 = drawQuestion(self.scene, "Extras/Comic_Book.ttf", "___")
        questionText3.pos = (WIDTH-250,130)

        continuebutton = drawButton(self.scene, "Extras/continue.png")
        continuebutton.pos = (WIDTH/2-100, HEIGHT-100)
        explainationText = drawCarry(self.scene, "Add the two numbers.")
        explainationText.pos = (0,0)
        explainationText6 = drawCarry(self.scene, "Click continue")
        explainationText6.pos = (0,100)
        explainationText7 = drawCarry(self.scene, "when you have your answer.")
        explainationText7.pos = (0,150)
        self.answer = drawQuestion(self, "Extras/Comic_Book.ttf", "")
        self.answer.pos = (WIDTH-230, 250)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        spyral.event.register('input.keyboard.down', self.updateAnswer)

    def updateAnswer(self, unicode, key):
        if unicode == u"\u0008":
            if len(self.answer.text) > 0:
                self.answer.update(self.answer.text[0:len(self.answer.text) - 1])
        elif key == 13 or key == 9:
            self.answer.update("")
            pass
        else:
            self.answer.update(self.answer.text + unicode)
