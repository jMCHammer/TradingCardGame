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
    char = ""
    opponentDead = False
    currentOpponent = "";


def loadResources():
		resources["background"] = spyral.image.Image("Extras/rsz_tundraclimate.png")
		resources["Arithmetic_u"] = spyral.image.Image("Extras/TradingCards/Arithmetic_u.png").scale(Vec2D(200,300))
		resources["Arithmetic_s"] = spyral.image.Image("Extras/TradingCards/Arithmetic_s.png").scale(Vec2D(200,300))
		resources["Geometry_u"] = spyral.image.Image("Extras/TradingCards/Geometry_u.png").scale(Vec2D(200,300))
		resources["Geometry_s"] = spyral.image.Image("Extras/TradingCards/Geometry_s.png").scale(Vec2D(200,300))
		resources["Wood"] = spyral.image.Image("Extras/wood1.png").scale(Vec2D(200,300))
		resources["GayRight"] = spyral.image.Image("Extras/stand.png")
		resources["GayLeft"] = spyral.image.Image("Extras/stand.png").flip(True,False)
		resources["GayRunRight"] = spyral.image.Image("Extras/run1.png")
		resources["GayRunLeft"] = spyral.image.Image("Extras/run1.png").flip(True,False)
		resources["ship"] = spyral.image.Image("Extras/rms.png")
		resources["woodbox"] = spyral.image.Image("Extras/box.png")
		resources["char1"] = spyral.image.Image("Extras/char1.png")
		resources["char2"] = spyral.image.Image("Extras/char2.png")
		resources["char3"] = spyral.image.Image("Extras/char3.png")
		resources["char4"] = spyral.image.Image("Extras/char4.png")
		resources["char5"] = spyral.image.Image("Extras/char5.png")
		resources["char6"] = spyral.image.Image("Extras/char6.png")
		resources["opponent1"] = spyral.image.Image("Extras/opponent1.png")
		resources["opponent2"] = spyral.image.Image("Extras/opponent2.png")
		resources["opponent3"] = spyral.image.Image("Extras/opponent3.png")
		resources["opponent4"] = spyral.image.Image("Extras/opponent4.png")
		resources["opponent5"] = spyral.image.Image("Extras/opponent5.png")
		resources["opponent6"] = spyral.image.Image("Extras/opponent6.png")
		resources["opponent1scaled"] = spyral.image.Image("Extras/opponent1scaled.png")
		resources["opponent2scaled"] = spyral.image.Image("Extras/opponent2scaled.png")
		resources["opponent3scaled"] = spyral.image.Image("Extras/opponent3scaled.png")
		resources["opponent4scaled"] = spyral.image.Image("Extras/opponent4scaled.png")
		resources["opponent5scaled"] = spyral.image.Image("Extras/opponent5scaled.png")
		resources["opponent6scaled"] = spyral.image.Image("Extras/opponent6scaled.png")
		resources["opponent1bg"] = spyral.image.Image("Extras/opponent1bg.png")
		resources["opponent2bg"] = spyral.image.Image("Extras/opponent2bg.png")
		resources["opponent3bg"] = spyral.image.Image("Extras/opponent3bg.png")
		resources["opponent4bg"] = spyral.image.Image("Extras/opponent4bg.png")
		resources["opponent5bg"] = spyral.image.Image("Extras/opponent5bg.png")
		resources["opponent6bg"] = spyral.image.Image("Extras/opponent6bg.png")

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
