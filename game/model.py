import spyral
from spyral import Vec2D
from collections import OrderedDict

resources  = {}
deck       = {}
looseCards = {
    "Arithmetic"       : ["Arithmetic",       80,  40], 
    "Geometry"         : ["Geometry",         100, 80]
}
allCards   = {
    "Arithmetic"       : ["Arithmetic",       80,  40], 
    "Geometry"         : ["Geometry",         100, 80],
    "Decimal Addition" : ["Decimal Addition", 90,  50], 
    "Algebra"          : ["Algebra",          100, 100]
    }

class Model:
    name = ""        
    gender = ""
    opponentDead = False


def loadResources():
	    resources["background"] = spyral.image.Image("Extras/rsz_tundraclimate.png")
	    resources["Arithmetic_u"] = spyral.image.Image("Extras/TradingCards/Arithmetic_u.png").scale(Vec2D(200,300))
	    resources["Arithmetic_s"] = spyral.image.Image("Extras/TradingCards/Arithmetic_s.png").scale(Vec2D(200,300))
	    resources["Geometry_u"] = spyral.image.Image("Extras/TradingCards/Geometry_u.png").scale(Vec2D(200,300))
	    resources["Geometry_s"] = spyral.image.Image("Extras/TradingCards/Geometry_s.png").scale(Vec2D(200,300))
	    resources["Hero_boy"] = spyral.image.Image("Extras/boy.png")
	    resources["Hero_girl"] = spyral.image.Image("Extras/girl.png")
	    resources["Wood"] = spyral.image.Image("Extras/wood1.png").scale(Vec2D(200,300))
	    resources["Gay"] = spyral.image.Image("Extras/stand.png")
	    resources["GayRun"] = spyral.image.Image("Extras/run1.png")
	    resources["woodbox"] = spyral.image.Image("Extras/box.png")

#Used to generate a saveCode which can be used to load a previous state
#If you wish to include more info in the saveCode, add a '.' and your choice of strings
def saveCode():
    deck_string = ""
    #sort by alphabetical keys
    orderedCards = OrderedDict(sorted(allCards.items(), key=lambda t: t[0]))
    for card in orderedCards:
        if card in deck:
            deck_string += "1"
        else:
            deck_string += "0"
    saveCode = str(int(deck_string, 2))
    ## To add more data, add
    # saveCode = saveCode + "." + newDataString
    return saveCode

#Used to load a previous game play state
# SaveCode : deckCardsString ## + "." + otherString 
def loadCode(saveCode):
    saveCode = saveCode.split('.')
    orderedCards = OrderedDict(sorted(allCards.items(), key=lambda t: t[0]))
    i = 0
    cards = bin(int(saveCode[0]))
    while cards:
        if int(cards[0]):
            card = orderedCards.items()[i]
            deck[card[0]] = card[1]
        i += 1
        cards = cards[1:]
    print deck
