import spyral

resources  = {}
deck       = {}
looseCards = {
    "Arithmetic"       : ["Arithmetic",       80,  40], 
    "Geometry"         : ["Geometry",         100, 80]
}
allCards   = {
#    "Arithmetic"       : ["Arithmetic",       80,  40], 
#    "Geometry"         : ["Geometry",         100, 80],
    "Decimal Addition" : ["Decimal Addition", 90,  50], 
    "Algebra"          : ["Algebra",          100, 100]
    }

joeyDeck = {
	"Arithmetic"       : ["Arithmetic",       80,  40]
	}

class Model:
    name = ""        
    gender = "" 

def loadResources():
	    resources["background"] = spyral.image.Image("Extras/rsz_tundraclimate.png")
	    resources["Arithmetic_u"] = spyral.image.Image("Extras/TradingCards/Arithmetic_u.png")
	    resources["Arithmetic_s"] = spyral.image.Image("Extras/TradingCards/Arithmetic_s.png")
	    resources["Geometry_u"] = spyral.image.Image("Extras/TradingCards/Geometry_u.png")
	    resources["Geometry_s"] = spyral.image.Image("Extras/TradingCards/Geometry_s.png")