import spyral
import model
import question
from spyral import Sprite, Vec2D
import math

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":0, "hard":0}

class lineGraph(Sprite):
	def __init__(self, View):
		super(lineGraph, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH, HEIGHT/90.0))
		self.anchor = 'center'
#		self.image.draw_circle((0,0,0), (self.width/2, self.height/2), WIDTH/50, 0,'topleft')
		self.image.draw_lines = ((0,0,0),
			[(0, 6),(WIDTH, 6)],
			10, False)

class circle(Sprite):
	def __init__(self, View):
		super(circle, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.circlePosition = (WIDTH/50,WIDTH/50)
		self.image.draw_circle((255,255,255), self.circlePosition, WIDTH/50, 0,'topleft')

class camera(spyral.View):
	def __init__(self, Scene):
		super(camera, self).__init__(Scene)
		self.circl = circle(self)
		self.camerapos = 0

		pass

class mainScreen(spyral.Scene):
	def __init__(self, q, difficulty):
		super(mainScreen, self).__init__(SIZE)
		self.background = spyral.Image(size=SIZE)
		self.background.fill((255,255,255))
		self.camera = camera(self)
		self.lin = lineGraph(self)
		self.lin.pos = (WIDTH/2, HEIGHT/2)
		pass