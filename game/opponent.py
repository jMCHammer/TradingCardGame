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

        if self.name is not None:
            #Needs to be changed to take in a deck
            pass

    #Randomly pick a card
    def pickCard(self):
        c = random.randint(0,len(self.deck)-1)
        self.selectedSubject = self.deck.keys()[c] 

    def answerQuestion(self):
        pass
