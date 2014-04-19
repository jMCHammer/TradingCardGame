import spyral

from spyral import Vec2D
from question import Question

class Card(spyral.Sprite):
    def __init__(self, subject):

        self.subject = subject
        self.path_u = "Extras/TradingCards/"+self.subject+"_u.png"
        self.path_s = "Extras/TradingCards/"+self.subject+"_s.png"
        self.difficultyList = ["easy", "medium", "hard"]
        self.damage = 10
        self.hp = 100
        self.alive = False
        self.clicked = False

    
    def handle_clicked(self, pos):
        if self.collide_point(pos):
            if self.clicked:
                self.clicked = False
                self.image = spyral.image.Image(self.path_u).scale(Vec2D(200,300))
            else:
                self.clicked = True
                self.image = spyral.image.Image(self.path_s).scale(Vec2D(200,300))

    def handle_deselect(self):
        self.clicked = False
        self.image = spyral.image.Image(self.path_u).scale(Vec2D(200,300))

    def setPos(self, x, y):
        self.x = x
        self.y = y


##TODO Should only be called once
    def draw(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image(self.path_u).scale(Vec2D(200,300))
        self.x = 10
        self.y = 10

        self.visible = False
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def isAlive(self, opponentDamage):
        self.hp = self.hp - opponentDamage
        if (self.hp <= 0):
            self.hp = 0
            self.alive = False

    def initQuestion(self, selectedDifficulty):
        self.question = Question(self.subject, selectedDifficulty)

