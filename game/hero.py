class Hero:
	"""This is our Hero class, otherwise known as the main character
	of the game.
	"""
	def __init__(self, name):
		self.name = name
		self.deck = []
		self.looseCards = []

	def addCardToDeck(self, card):
		newcard = self.looseCards.index(card)
		newcard.alive = True
		self.deck.append(newcard)
		self.looseCards.remove(card)

	def addCardToLooseCards(self, card):
		self.looseCards.append(card)

	def removeCardFromDeck(self, card):
		newcard = self.deck.index(card)
		newcard.alive = False
		self.looseCards.append(newcard)
		self.deck.remove(card)

	def isAlive(self):
		for card in deck:
			if (card.alive):
				return True
		return False
