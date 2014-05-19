import spyral
import model
import random

WIDTH    = 1200

class Opponent(spyral.Sprite):
    """This is our Opponent class, used to hold important information about the character.
    """
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.name = model.currentOpponent
        print self.name
        self.image = model.resources[model.currentOpponent + "scaled"]
        self.pos = (50, 50)
        self.layer = "text"
        
        #self.deck = {}
        n = int(self.name[len(self.name)-1])
        if n < 5:
            subject = model.allCards.keys()[n-1]
            self.deck = {subject : model.allCards[subject]}
        elif n < 6: 
            self.deck = {model.allCards.keys()[2]: model.allCards[model.allCards.keys()[2]],
                         model.allCards.keys()[3]: model.allCards[model.allCards.keys()[3]]}
        else: 
            self.deck = {model.allCards.keys()[3]: model.allCards[model.allCards.keys()[3]],
                         model.allCards.keys()[4]: model.allCards[model.allCards.keys()[4]]}
        self.pickCard()

    #Randomly pick a card
    def pickCard(self):
        c = random.randint(0,len(self.deck)-1)
        self.selectedSubject = self.deck.keys()[c] 
        return self.selectedSubject

    def answerQuestion(self):
        #Randomly pick a difficulty
        # 60% easy, 30% medium, 10% hard
        # 1 = easy, 2 = medium, 3 = hard
        self.selectedDifficulty = 1

        c = random.randint(1, 10) 
        if c > 6: 
            if c > 9:
                self.selectedDifficulty = 2
            else:
                self.selectedDifficulty = 3

        # 1 <= c <= 10
        rnge = self.selectedDifficulty*10
        t = random.randint(1, rnge)
        # 1 <= t <= {10, 20, 30}

        # AI logic

        # if t > {3, 13, 23}

        # if easy,   70% chance of answering correctly
        # if medium, 35% chance of answering correctly
        # if hard, 17.5% chance of answering correctly
        if t >= (rnge - 7):
            return True
        else:
            return False
