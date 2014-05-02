#I am thinking of how to approach this... :(
import spyral
import model
import question
from spyral import Sprite, Vec2D

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class BoatFloor(Sprite):
	def __init__(self, Scene):
		super(BoatFloor,self).__init__(Scene)
		self.numFloor = 0 #or 2
		self.num = 0 #from 0~9
		self.image = model.resources["Wood"].scale((WIDTH/19, HEIGHT/32))

	def setNumber(self, fl, num):
		self.numFloor = fl
		self.num = num * pow(10,numFloor)
		pass

class Boat(Sprite):
	def __init__(self, Scene):
		super(Boat,self).__init__(Scene)
		pass

class MovingPiece(Sprite):	
	def __init__(self, Scene):
		super(MovingPiece, self).__init__(Scene)
		self.dx = 0
		self.move = False
		self.direction = "right"
		spyral.event.register("input.keyboard.down.left", self.moveLeft)
		spyral.event.register("input.keyboard.down.right", self.moveRight)
		spyral.event.register("input.keyboard.up.left", self.stopMove)
		spyral.event.register("input.keyboard.up.right", self.stopMove)
		spyral.event.register("director.update", self.Update)

	def moveLeft(self):
		self.move = "left"
		self.direction = "left"
	def moveRight(self):
		self.move = "right"
		self.direction = "right"
	def stopMove(self):
		self.move = False

	def Update(self):
		if(self.move == "left"):
			self.pos = (self.pos[0] - self.dx, self.pos[1])
		elif(self.move == "right"):
			self.pos = (self.pos[0] + self.dx, self.pos[1])

	def initialPos(self, pos):
		self.position = pos


class Box(MovingPiece):
	def __init__(self, Scene, boxWeight):
		super(Box,self).__init__(Scene)
		self.pickedUp = False
		self.x = 0
		self.image = model.resources["woodbox"].scale((HEIGHT/32, HEIGHT/32))

class Man(MovingPiece):
	def __init__(self, Scene):
		super(Man, self).__init__(Scene)
		self.pickingUp = False
		self.dx = 5 # how fast this dick is moving
		self.x = 0
		self.floor = 0;  # which floor is he at
		self.images = [model.resources["GayRight"].scale((HEIGHT/32, HEIGHT/16)),
						model.resources["GayLeft"].scale((HEIGHT/32, HEIGHT/16)),
						model.resources["GayRunRight"].scale((HEIGHT/16, HEIGHT/16)),
						model.resources["GayRunLeft"].scale((HEIGHT/16, HEIGHT/16))]
		self.image = self.images[0]

		spyral.event.register("input.keyboard.down.down", self.moveDown)
		spyral.event.register("input.keyboard.down.up", self.moveUp)
		spyral.event.register("director.update", self.imageUpdate)

	def moveUp(self):
		if(self.floor > 0):
			self.floor -= 1

	def moveDown(self):
		if(self.floor < 3):
			self.floor += 1

	def imageUpdate(self):
		if(not self.move):
			if self.direction == "right":
				self.image = self.images[0]
			else:
				self.image = self.images[1]
		else:
			if self.direction == "right":
				self.image = self.images[2]
			else:
				self.image = self.images[3]	

class DivisionScreen(spyral.Scene):
	def __init__(self, q):
		global manager
		super(DivisionScreen, self).__init__(SIZE)
		model.loadResources()
		self.background = spyral.Image(size=SIZE)
		self.background.fill((0,0,0))
		self.question = q
		self.numerator = self.question.randomNumTwo
		self.divisor = self.question.randomNumOne

		spyral.event.register("director.update", self.Update)

		self.floors = []
		self.boxes = []

		for f in range(1, 5):
			floor = []
			for i in range(0, 19):
				floormat = BoatFloor(self)
				floormat.pos = (i * WIDTH/19, f * HEIGHT/4 - floormat.image.height)
				floor.append(floormat)
			self.floors.append(floor)

		for i in range(1, 5):
				box = Box(self, self.divisor)
				box.pos = (WIDTH/2, self.floors[i - 1][0].pos[1] - HEIGHT/32)
				self.boxes.append(box)

		self.man = Man(self)
		self.man.pos = (WIDTH/19, self.floors[self.man.floor][0].pos[1] - HEIGHT/16)

	def Update(self):
		self.man.pos = (self.man.pos[0], self.floors[self.man.floor][0].pos[1] - HEIGHT/16)