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
        self.image = model.resources[model.currentOpponent + "scaled"]
        self.pos = (50, 50)
        self.layer = "text"


        #self.deck = {}
        self.deck = {"Arithmetic" : ["Arithmetic", 80,  40]}
        self.selectedSubject = "Arithmetic"
        # 1 = easy, 2 = medium, 3 = hard
        self.selectedDifficulty = 1

        if self.name is not None:
            #Needs to be changed to take in a deck
            pass

    #Randomly pick a card
    def pickCard(self):
        c = random.randint(0,len(self.deck)-1)
        self.selectedSubject = self.deck.keys()[c] 

    def answerQuestion(self):
        #Randomly pick a difficulty
        # 60% easy, 30% medium, 10% hard
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
