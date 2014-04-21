import spyral
import model

class Opponent(spyral.Sprite):
	"""This is our Opponent class, used to hold important information about the character.
	"""
	def __init__(self, name):
		self.name = name
		if name == "Youngster Joey":
			self.deck = model.joeyDeck

	def isAlive(self):
		for card in self.deck:
			if (card.alive):
				return True
		return False
	
