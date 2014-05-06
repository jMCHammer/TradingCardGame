import spyral
import model


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


# TODO implement AI logic
    def pickCard(self):
        self.selectedSubject = "Arithmetic"

    def answerQuestion(self):
        pass

