from card import Card

class Hero:
    """This is our Hero class, otherwise known as the main character
    of the game.
    """
    deck       = {}
    looseCards = {}
    allCards   = {
        "Addition" : Card("Addition"), 
        "Decimal Addition" : Card("Decimal Addition"), 
        "Algebra" : Card("Algebra"), 
        "Geometry" : Card("Geometry")}

    def __init__(self, name):
        self.name = name

    def addCardToDeck(self, subject):
        if len(self.deck) < 3 and subject in self.looseCards:
            newcard = self.looseCards[subject]
            newcard.alive = True
            self.deck[subject] = newcard
            del self.looseCards[subject]
##
            print (self.looseCards)
            print (self.deck)
##

            ## Return so referencing class can modify Card
            return newcard
        else:
            print ("A deck can't have more than 3 cards OR Card isn't in looseCards")

    def addCardToLooseCards(self, subject):
        if subject in self.allCards:
            self.looseCards[subject] = self.allCards[subject]

            ## Return so referencing class can modify Card
            return self.allCards[subject]
        else:
            print ("Card doesn't exist")

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

    def isAlive(self):
        for card in self.deck:
            if (card.alive):
                return True
        return False
