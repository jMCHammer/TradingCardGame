#I am thinking of how to approach this... :(

import Random
import spyral
import model
import Question
from spyral import Sprite

class BoatFloor(Sprite):
	def __ init__(self, Scene):
		super(Boar,self).__init__(self, Scene)
		pass

class Boat(Sprite):
	def __init__(self, Scene):
		super(Boat,self).__init__(self, Scene)
		pass

class Box(Sprite):
	def __init__(self, Scene, boxWeight):
		super(Box,self).__init__(self, Scene)
		self.pickedUp = False
		pass

class Man(Sprite):
	def __init__(self, Scene):
		super(Man, self).__init__(self, Scene)
		pass


class DivisionScreen(spyral.Scene):
	def __init__(self, SIZE, q):
		global.manager
		super(DivisionScreen, self).__init__(self, SIZE)
		self.background = model.resource["background"]
		self.question = q
		self.numerator = self.question.randomNumTwo
		self.divisor = self.question.randomNumOne