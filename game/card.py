import spyral
import model

from spyral import Vec2D
#from question import Question

class Card(spyral.Sprite):
    def __init__(self, Scene, subject, health, damage):
        spyral.Sprite.__init__(self, Scene)
        self.image = model.resources[subject + "_u"].scale(Vec2D(200,300))
        self.x = 10
        self.y = 10

        self.subject = subject
        self.health = health
        self.damage = damage

        self.difficultyList = ["easy", "medium", "hard"]
        self.alive   = True
        self.clicked = False
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

##TODO Temporary solution until Question logic is finished
## Should initQuestion after a player chooses it's card difficulty
        self.initQuestion("easy")
##


#### Determines whether a mouse click has selected this card
    def handle_clicked(self, pos):
        if self.collide_point(pos):
            if self.clicked:
                self.handle_deselect()
            else:
                self.clicked = True
                self.image = model.resources[self.subject + "_s"].scale(Vec2D(200,300))

#### Used to deselect an active card
    def handle_deselect(self):
        self.clicked = False
        self.image = model.resources[self.subject + "_u"].scale(Vec2D(200,300))

#### Initialized the Question for the corresponding card
## TODO
    def initQuestion(self, selectedDifficulty):
        self.question = "25.0 + 25.0 = "
        self.answer = 50
#        self.question = Question(self.subject, selectedDifficulty)





