import spyral
from card import Card

class Hero(spyral.Sprite):
    """This is our Hero class, otherwise known as the main character
    of the game.
    """
    deck       = {}
    looseCards = {}
    allCards   = {
        "Arithmetic"       : Card("Arithmetic", 80, 40), 
        "Geometry"         : Card("Geometry", 100, 80),
        "Decimal Addition" : Card("Decimal Addition", 90, 50), 
        "Algebra"          : Card("Algebra", 100, 100)}

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


########## EditCollectionScreen functions #####################################
#### Draws card in appropriate scene 
    def draw(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        if (self.gender == "boy"):
            self.image = spyral.image.Image("Extras/boy.png")
        if (self.gender == "girl"):
            self.image = spyral.image.Image("Extras/girl.png")

#### Adds card from looseCards to Deck
    def addCardToDeck(self, subject):
        if len(self.deck) < 3 and subject in self.looseCards:
            newcard = self.looseCards[subject]
            newcard.alive = True
            self.deck[subject] = newcard
            del self.looseCards[subject]

            ## Return so referencing class can modify Card
            return newcard
        else:
            print ("A deck can't have more than 3 cards OR Card isn't in looseCards")

#### Adds new card to looseCards from allCards
    def addCardToLooseCards(self, subject):
        if subject in self.allCards:
            self.looseCards[subject] = self.allCards[subject]

            ## Return so referencing class can modify Card
            return self.allCards[subject]
        else:
            print ("Card doesn't exist")

### Adds card to looseCards from Deck
    def removeCardFromDeck(self, subject):
        if subject in self.deck:
            newcard = self.deck[subject]
            newcard.alive = False
            self.looseCards[subject] = newcard
            del self.deck[subject]
            
            ## Return so referencing class can modify Card
            return newcard
        else:
            print ("subject isn't in deck")
########## </EditCollectionScreen> ############################################

########## FaceOffScreen functions ############################################
#### Used for Battles to determine whether all cards are alive
    def isAlive(self):
        for card in self.deck:
            if (card.alive):
                return True
        return False
