#I am thinking of how to approach this... :(
import spyral
import model
import question
from spyral import Sprite, Vec2D

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 675
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":1, "hard":2}


class drawFont(Sprite):
    def __init__(self, Scene, text, font):
        super(drawFont,self).__init__(Scene)
        self.f = font
        self.text = text
        self.image = self.f.render(self.text)

    def update(self, string):
        self.text = string
        self.image = self.f.render(self.text)

class BoatFloor(Sprite):
	def __init__(self, Scene):
		super(BoatFloor,self).__init__(Scene)
		self.numFloor = 0 #from -2~1
		self.num = 0 #from 0~9
		self.image = model.resources["Wood"].scale((WIDTH/19, HEIGHT/32))

	def setNumber(self, fl, num):
		self.numFloor = fl
		self.num = num * pow(10,self.numFloor)
		pass

	def rescale(self,size):
		self.image = model.resources["Wood"].scale(size)

class Boat(Sprite): #HAVENT BEEN USED YET
	def __init__(self, Scene):
		super(Boat,self).__init__(Scene)
		pass

class MovingPiece(Sprite):	
	def __init__(self, Scene):
		super(MovingPiece, self).__init__(Scene)
		self.sc = Scene
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
		self.x = 0
		self.dx = 0
		self.floor = 0
		self.pickedUp = False
		self.image = model.resources["woodbox"].scale((HEIGHT/32, HEIGHT/32))

	def pickUp(self):
		self.dx = 5
		self.pickedUp = True

	def putDown(self):
		self.dx = 0
		self.pickedUp = False

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
		spyral.event.register("input.keyboard.down.space", self.pickUp)

	def pickUp(self):

		if(not self.pickingUp):
			for box in self.sc.boxes:
				if self.sc.collide_sprites(self.sc.man, box):
					box.pickUp()
					box.pos = (self.pos[0], self.pos[1] - box.height)
					self.pickingUp = True
					print("You are picking up the box...")
					break
		else:
			for box in self.sc.boxes:
				if box.pickedUp:
					self.pickingUp = False
					box.putDown()
					box.pos = (self.pos[0], self.pos[1] + HEIGHT/16 - box.height)
					break
		pass

	def moveUp(self):
		if(self.floor > 0 and not self.pickingUp):
			self.floor -= 1

	def moveDown(self):
		if(self.floor < 2 and not self.pickingUp):
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
	def __init__(self, q, difficulty):
		global manager
		super(DivisionScreen, self).__init__(SIZE)
		model.loadResources()
		self.difficulty = DIFFICULTY[difficulty]
		self.background = spyral.Image(size=SIZE)
		self.background.fill((0,0,0))
		self.question = q
		self.numerator = self.question.randomNumTwo
		self.divisor = self.question.randomNumOne
		self.answer = 0

		spyral.event.register("director.update", self.Update)

		self.floors = []
		self.boxes = []
		self.texts = []

		self.answerText = drawFont(self, " Goal: " + str(self.numerator), spyral.Font(FONT, 30, (255,255,255)))
		self.weightText = drawFont(self, " Box Weight: " + str(self.divisor), spyral.Font(FONT, 30, (255,255,255)))
		self.weightText.pos = (self.answerText.width, 0)
		self.currentText = drawFont(self, " Current: " + str(self.answer), spyral.Font(FONT, 30, (255,255,255)))
		self.currentText.pos = (self.answerText.width + self.weightText.width, 0)

		for f in range(1, 4):
			length = 19 if self.difficulty > 0 else 10
			modifier = -9 if self.difficulty > 0 else 0
			scalar = (WIDTH/length, HEIGHT/32)
			floor = []
			for i in range(0, length):
				floormat = BoatFloor(self)
				floormat.setNumber(2 - f, i + modifier)
				floormat.pos = (i * WIDTH/length, f * HEIGHT/3 - floormat.image.height)
				floormat.rescale(scalar)
				floor.append(floormat)
				t = drawFont(self, str(floormat.num), spyral.Font(FONT, 15, (255,255,255)))
				t.pos = (floormat.pos[0], floormat.pos[1] - floormat.image.height)
				self.texts.append(t)
			self.floors.append(floor)

		for i in range(1, 4):
				box = Box(self, self.divisor)
				box.pos = (WIDTH/19 * 9 + box.width/2 if self.difficulty > 0 else 0 + box.width/2,
							self.floors[i - 1][0].pos[1] - HEIGHT/32)
				box.floor = i - 1
				self.boxes.append(box)

		self.man = Man(self)
		self.man.pos = (WIDTH/19, self.floors[self.man.floor][0].pos[1] - HEIGHT/16)

	def Update(self):
		length = 19 if self.difficulty > 0 else 10
		modifier = -9 if self.difficulty > 0 else 0
		self.man.pos = (self.man.pos[0], self.floors[self.man.floor][0].pos[1] - HEIGHT/16)
		answer = 0
		for box in self.boxes:
			answer += int((box.pos[0]/(WIDTH/length)) + modifier) * self.divisor * pow(10, (1 - box.floor))
		self.answer = answer
		self.currentText.update(" Current: " + str(self.answer))