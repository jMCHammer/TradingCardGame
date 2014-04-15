import spyral

from model import Model

# View Imports
from startScreen  import StartScreen
from nameScreen   import NameScreen
from genderScreen import GenderScreen

class Controller(spyral.Scene):
    def __init__(self, *args, **kwargs):
        self.model = Model()
        self.startScreen()
###############################################################################
# Functions
    def startGame(self):
        name = raw_input("Enter your name:")
        self.model.initHero(name)

    def choosePlayer(self):
        #TODO
        #show Player view
        pass

    # Edit the Player's Deck from the list of available cards
    def editDeck(self):
        #TODO
        #start EditDeck View

        #Move cards to and from Deck
        command = raw_input("'Remove' or 'Add' from deck?")
        card = raw_input("Which card?")
        if command == 'Remove':
            self.model.hero.removeCardFromDeck(card)
        elif command == 'Add':
            self.model.hero.addCardToDeck(card)

    def foundNewCard(self):
		#TODO
        #choose random card from listof allCards in Model
        card = self.model.allCards[0]
        self.model.hero.addCardToLooseCards(card)


