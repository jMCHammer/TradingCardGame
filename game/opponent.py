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
        opp = int(self.name[len(self.name)-1])
        if opp == 1:
            self.deck = {"Addition": model.allCards["Addition"]}
        elif opp == 2:
            self.deck = {"Subtraction": model.allCards["Subtraction"]}
        elif opp == 3:
            self.deck = {"Multiplication": model.allCards["Multiplication"]}
        elif opp == 4:
            self.deck = {"Integer": model.allCards["Integer"]}
        elif opp == 5:
            self.deck = {"Multiplication": model.allCards["Multiplication"],
                         "Division" : model.allCards["Division"]}
        elif opp == 6:
            self.deck = {"Statistics": model.allCards["Statistics"]}

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
            self.correct = True
            return True
        else:
            self.correct = False
            return False
