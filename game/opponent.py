import spyral
import model


WIDTH    = 1200

class Opponent(spyral.Sprite):
	"""This is our Opponent class, used to hold important information about the character.
	"""
	def __init__(self, Scene, name):
		spyral.Sprite.__init__(self, Scene)
		self.name = name
		self.image = model.resources[name]
		self.deck = {}
		if name == "Youngster Joey":
			self.deck = model.joeyDeck

# TODO implement AI logic
	def pickCard(self):
		self.selectedSubject = "Arithmetic"

	def answerQuestion(self):
		pass

