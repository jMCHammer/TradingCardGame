import spyral
import model

from question import Question

class Card(spyral.Sprite):
    def __init__(self, Scene, subject, health, damage):
        spyral.Sprite.__init__(self, Scene)
        self.image = model.resources[subject + "_u"]
        self.x = 10
        self.y = 10

        self.subject = subject
        self.health = health
        self.damage = damage

        self.difficultyList = ["easy", "medium", "hard"]
        self.alive   = True
        self.clicked = False
        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def applyDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

##TODO Temporary solution until Question logic is finished
## Should initQuestion after a player chooses it's card difficulty
       # self.initQuestion("easy")
##


#### Determines whether a mouse click has selected this card
    def handle_clicked(self, pos):
        if self.collide_point(pos):
            if self.alive and self.clicked:
                self.handle_deselect()
            elif self.alive:
                self.clicked = True
                self.image = model.resources[self.subject + "_s"]

#### Used to deselect an active card
    def handle_deselect(self):
        self.clicked = False
        self.image = model.resources[self.subject + "_u"]

#### Initialized the Question for the corresponding card
## TODO
    def initQuestion(self, selectedDifficulty):
        self.q = Question(self.subject, selectedDifficulty)
        print self.q.answer
        print self.q.text
        self.question = self.q.text
        self.answer = self.q.answer
#        quiz.
#        self.question = Question(self.subject, selectedDifficulty)





