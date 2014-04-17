import spyral

from question import Question

class drawFont(spyral.Sprite):
    def __init__(self, Scene, font, text, size):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, size)
        self.image = f.render(text)
        self.layer = "text"

class Card(spyral.Sprite):
    def __init__(self, subject):

        self.subject = subject
        self.difficultyList = ["easy", "medium", "hard"]
        self.damage = 10
        self.hp = 100
        self.alive = False
        self.clicked = False

    
    def handle_clicked(self, pos):
        if self.collide_point(pos):
            self.clicked = True

##
    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.text.pos = (self.x+10, self.y+10)

##TODO Should be private
    def draw(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.Image(size=(100, 140)).fill((139, 69, 19))
        self.x = 10
        self.y = 10
        self.text = drawFont(Scene, "Extras/Comic_Book.ttf", self.subject, 15)
        self.text.pos = (self.x+10, self.y+10)
        self.visible = False

        spyral.event.register("input.mouse.down.left", self.handle_clicked)

    def isAlive(self, opponentDamage):
        self.hp = self.hp - opponentDamage
        if (self.hp <= 0):
            self.hp = 0
            self.alive = False

    def initQuestion(self, selectedDifficulty):
        self.question = Question(self.subject, selectedDifficulty)

