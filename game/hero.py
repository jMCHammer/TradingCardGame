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
        self.char = model.char
        self.image  = model.resources[self.char]
