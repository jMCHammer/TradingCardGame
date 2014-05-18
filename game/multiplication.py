import spyral
import model
import question
from spyral import Sprite, Vec2D
import math

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":1, "hard":1}

class drawFont(Sprite):
	def __init__(self, Scene, text, font):
		super(drawFont,self).__init__(Scene)
		self.f = font
		self.text = text
		self.image = self.f.render(self.text)

	def update(self, string):
		self.text = string
		self.image = self.f.render(self.text)

class measureLine(Sprite):
	def __init__(self, View, pos):
		super(measureLine, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH/240.0, HEIGHT/30.0))
		self.anchor = 'center'
		self.image.draw_lines((0,0,0),[(WIDTH/480, 0),(WIDTH/480, HEIGHT/30.0)],5, False)
		self.pos = pos

class ironBoard(spyral.View):
	def __init__(self, View, diff):
		super(ironBoard, self).__init__(View)
		self.board = Sprite(self)
		self.board.image = spyral.Image(size = (3*WIDTH/2.0, HEIGHT/30.0))
		self.board.image.draw_rect((120,120,120),(0,0),(3*WIDTH/2.0,HEIGHT/30.0),0,'topleft')
		self.board.layer = 'bottom'
		self.anchor = 'midleft'
		self.measures = []
		self.diff = DIFFICULTY[diff]

		for i in range(0,4 + self.diff):
			measure = measureLine(self, (i * 3*WIDTH/8.0,HEIGHT/60.0))
			measure.layer = 'top'
			self.measures.append(measure)

		self.layers = ['top', 'bottom']
		spyral.event.register("director.update", self.update)
		spyral.event.register("input.keyboard.down.left", self.scroll)

		self.scroll = False
		self.dist = 3*WIDTH/8.0
		self.time = 30.0
		self.tick = 0.0
		self.dx = self.dist/self.time
		self.currentPlate = 0

	def update(self):
		if self.scroll and self.currentPlate < 3 + self.diff:
			if(self.time > self.tick):
				self.x -= self.dx
				self.tick += 1
			else:
				self.scroll = False
				self.tick = 0.0
				self.currentPlate += 1

	def scroll(self):
		if not self.scroll and not self.scene.hammer.hammertime:
			self.scroll = True
		pass

class ironHammer(spyral.View):
	def __init__(self, Scene):
		super(ironHammer, self).__init__(Scene)
		self.head = Sprite(self)
		self.head.image = spyral.Image(size = (WIDTH/10.0, HEIGHT/4.0))
		self.head.image.fill((20,20,20))
		self.head.anchor = 'topleft'
		self.head.pos = (HEIGHT/3.0,0)
		self.handle = Sprite(self)
		self.handle.image = spyral.Image(size = (HEIGHT/3.0,WIDTH/20.0))
		self.handle.image.fill((51,0,0))
		self.handle.anchor = 'topleft'
		self.handle.pos = (0, (HEIGHT/4.0 - WIDTH/20.0)/2)
		self.anchor = "bottomleft"

		self.number = 0

		self.hammertime = False
		self.tick = 0.0
		self.t = 20.0
		self.p = 3.0
		self.h = 2*HEIGHT/4.0 - HEIGHT/4.5

		spyral.event.register("director.update", self.update)
		spyral.event.register("input.keyboard.down.down", self.hammerTime)

	def setNumber(self, number):
		self.number = number

	def update(self):
		if self.hammertime:
			if self.tick < self.p:
				self.y += self.h/self.p
			elif self.tick < self.t:
				self.y -= self.h/(self.t - self.p)
			else:
				self.hammertime = False
				self.tick = -1.0
			if self.tick == self.t - 1:
				pass
				# NEED TO IMPLEMENT DECREASE
			self.tick += 1

	def hammerTime(self):
		if not self.hammertime and not self.scene.board.scroll and (self.scene.board.currentPlate < 3 + self.scene.board.diff):
			self.hammertime = True

class mainScreen(spyral.Scene):
	def __init__(self, q, diff):
		super(mainScreen, self).__init__(SIZE)
		self.background = spyral.Image(size = SIZE)
		self.background.fill((255,255,255))
		self.board = ironBoard(self,diff)
		self.board.pos = (WIDTH/4,3*HEIGHT/4.0)
		self.hammer = ironHammer(self)
		self.hammer.pos = (WIDTH/10.0,HEIGHT/4.5)
		
		self.iron = Sprite(self)
		self.iron.image = spyral.Image(size = (WIDTH/3.0,HEIGHT/4.5))
		self.iron.image.fill((20,20,20))
		self.iron.anchor = 'topleft'
		self.iron.pos = (self.hammer.head.x + WIDTH/40.0, HEIGHT/30.0 + 3*HEIGHT/4.0)