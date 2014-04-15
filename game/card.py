from question import Question

class Card:
    def __init__(self, subject):
        self.subject = subject
        self.difficultyList = ["easy", "medium", "hard"]
        self.damage = 10
        self.hp = 100
        self.alive = True

    def isAlive(self, opponentDamage):
        self.hp = self.hp - opponentDamage
        if (self.hp <= 0):
            self.hp = 0
            self.alive = False
        

    def initQuestion(self, selectedDifficulty):
        self.question = Question(self.subject, selectedDifficulty)

