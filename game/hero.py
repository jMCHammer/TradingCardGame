import spyral
import model

class Hero(spyral.Sprite):
    """This is our Hero class, otherwise known as the main character
    of the game.
    """
    cards = []
    def __init__(self, Scene):
        spyral.Sprite.__init__(self,Scene)
        self.name   = model.name
        self.gender = model.gender
        self.image  = spyral.image.Image("Extras/" + self.gender + ".png")

    #Used for Battle Screen
    def isAlive(self):
        for card in self.cards:
            if (card.alive):
                return True
        return False