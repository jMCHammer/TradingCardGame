import spyral
from spyral import Vec2D

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

joeyDeck = {
	"Arithmetic"       : ["Arithmetic",       80,  40]
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
	    resources["Youngster Joey"] = spyral.image.Image("Extras/Youngster_Joey.png").scale(Vec2D(8, 10))
	    resources["Wood"] = spyral.image.Image("Extras/wood1.png").scale(Vec2D(200,300))
	    resources["GayRight"] = spyral.image.Image("Extras/stand.png")
	    resources["GayLeft"] = spyral.image.Image("Extras/stand.png").flip(True,False)
	    resources["GayRunRight"] = spyral.image.Image("Extras/run1.png")
	    resources["GayRunLeft"] = spyral.image.Image("Extras/run1.png").flip(True,False)
	    resources["woodbox"] = spyral.image.Image("Extras/box.png")
	    resources["ship"] = spyral.image.Image("Extras/rms.png")
