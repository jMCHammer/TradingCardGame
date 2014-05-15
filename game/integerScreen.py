import spyral
import model
import question
from spyral import Sprite, Vec2D
import math
import random
import model

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":0, "hard":0}


#steve's adventure
class drawFont(Sprite):
    def __init__(self, Scene, text, font):
        super(drawFont,self).__init__(Scene)
        self.f = font
        self.text = text
        self.image = self.f.render(self.text)

    def update(self, string):
        self.text = string
        self.image = self.f.render(self.text)

class Nick(Sprite):
	def __init__(self,View):
		super(Nick, self).__init__(View)
		self.anchor = "midbottom"
		self.images = [model.resources["GayRight"].scale((HEIGHT/8, HEIGHT/4)),
						model.resources["GayLeft"].scale((HEIGHT/8, HEIGHT/4)),]
		self.direction = "right"
		self.image = self.images[0]
#Man dog Steve
class Steve(spyral.View):
	def __init__(self, Scene):
		super(Steve, self).__init__(Scene)
		self.direction = "left"
		#body
		self.body = SteveBody(self, (WIDTH/2.0, 6*HEIGHT/7.0 -WIDTH/35.0))
		self.body.pos = (WIDTH/2.0, 6*HEIGHT/7.0 -WIDTH/35.0)
		#claws
		self.leg1 = SteveLeg(self)
		self.leg1.pos = (self.body.x - WIDTH/70.0, self.body.y+WIDTH/42.5)
		self.leg2 = SteveLeg(self)
		self.leg2.pos = (self.body.x + WIDTH/70.0, self.body.y+WIDTH/42.5)
		#head
		self.head = Sprite(self)
		self.head.image = spyral.Image(size=(WIDTH/25.0, WIDTH/40.0))
		self.head.image.draw_ellipse((153,76,0), (0,0), self.head.size, 0)
		self.head.anchor = 'center'
		self.head.angle = math.pi/18.0
		self.head.pos = (self.body.x - WIDTH/44.0, self.body.y-WIDTH/75.0)
		#tail
		self.tail = Sprite(self)
		self.tail.image = spyral.Image(size=(WIDTH/85.0,WIDTH/30.0))
		self.tail.image.draw_ellipse((153,76,0), (0,0), self.tail.size, 0)
		self.tail.anchor = 'center'
		self.tail.angle = -math.pi/5.0
		self.tail.pos = (self.body.x + WIDTH/38.0, self.body.y-WIDTH/90.0)
		spyral.event.register("input.keyboard.down.space", self.jump)
		spyral.event.register("input.keyboard.down.left", self.left)
		spyral.event.register("input.keyboard.down.right", self.right)

	def left(self):
		self.direction = "left"

	def right(self):
		self.direction = "right"

	def jump(self):
		self.body.jump()

	def update(self):
		if not self.body.movey:
			self.leg1.y = self.body.y + WIDTH/42.5
			self.leg2.y = self.body.y + WIDTH/42.5
			self.leg1.x = self.body.x - WIDTH/70.0
			self.leg2.x = self.body.x + WIDTH/70.0
			self.leg1.angle = math.pi
			self.leg2.angle = math.pi
		elif self.body.movey == "jump":
			self.leg1.y = self.body.y + WIDTH/55.5
			self.leg2.y = self.body.y + WIDTH/55.5
			self.leg1.x = self.body.x - WIDTH/55.0
			self.leg2.x = self.body.x + WIDTH/55.0
			self.leg1.angle = -math.pi/6.0
			self.leg2.angle = math.pi/6.0
		if self.direction == "left":
			self.head.pos = (self.body.x - WIDTH/44.0, self.body.y-WIDTH/75.0)
			self.head.angle = math.pi/18.0
			self.tail.pos = (self.body.x + WIDTH/38.0, self.body.y-WIDTH/90.0)
			self.tail.angle = -math.pi/5.0
		elif self.direction == "right":
			self.head.pos = (self.body.x + WIDTH/44.0, self.body.y-WIDTH/75.0)
			self.head.angle = -math.pi/18.0
			self.tail.pos = (self.body.x - WIDTH/38.0, self.body.y-WIDTH/90.0)
			self.tail.angle = +math.pi/5.0

class SteveBody(Sprite):
	def __init__(self, View, pos):
		super(SteveBody, self).__init__(View)
		self.anchor = 'center'
		self.image = spyral.Image(size=(WIDTH/25.0, WIDTH/25.0))
		self.image.draw_ellipse((153,76,0), (0,WIDTH/25.0 - WIDTH/35.0), (WIDTH/25.0, WIDTH/35.0), 0,'topleft')
		self.ty = 0
		self.vy = 10
		self.movey = False
		self.origpos = pos
		self.tempx = pos[0]
		self.tempy = pos[1]
		spyral.event.register("director.update",self.update)

	def jump(self):
		if self.movey != "jump" and (self.ty < 3 or self.ty > 23):
			self.movey = "jump"
			self.ty = 0
			self.tempy = self.origpos[1]

	def update(self):
		if self.movey != "jump":
			 if self.ty >= 25:
			 	self.ty = 0
			 else:
			 	he = WIDTH/15.0
			 	a = -8.0*he/pow(24.0,2)
			 	b = 4.0*he/24.0
				dy = a*self.ty + b
			 	self.tempy -= dy
			 	self.ty += 1
		elif self.movey == "jump":
			if self.ty >= 25:
				self.ty = 0
				self.movey = False
			else:
				he = WIDTH/3.0
				a = -8.0*he/pow(24.0,2)
				b = 4.0*he/24.0
				dy = a*self.ty + b
				self.tempy -= dy
				self.ty += 1

class SteveLeg(Sprite):
	def __init__(self, View):
		super(SteveLeg, self).__init__(View)
		self.anchor = 'center'
		self.image = spyral.Image(size=(WIDTH/75.0, WIDTH/50.0))
		self.image.draw_ellipse((153,76,0), (0,0), self.size, 0)

class measureLine(Sprite):
	def __init__(self, View, pos):
		super(measureLine, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH/240, HEIGHT/45))
		self.anchor = 'center'
		self.image.draw_lines((0,0,0),[(WIDTH/480, 0),(WIDTH/480, HEIGHT/45)],5, False)
		self.pos = pos

class Line(Sprite):
	def __init__(self, View):
		super(Line, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH*5, HEIGHT/180))
		self.anchor = 'topleft'
		self.image.draw_lines((0,0,0),[(0, 0),(self.width, 0)],5, False)

class Ball(Sprite):
	def __init__(self, View):
		super(Ball, self).__init__(View)
		self.anchor = 'midbottom'
		self.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.image.draw_circle((random.randint(30,225),random.randint(30,225),random.randint(30,225)),
								(WIDTH/50,WIDTH/50), WIDTH/50, 0, 'topleft')
		self.number = 0
		self.ay = 0
		self.by = 0
		self.ax = 0
		self.bx = 0
		self.t = 0
		self.limt = 300.0
		
		self.visible = False

	def updateFormula(self, number):
		self.number = number
		t = self.limt
		#dy
		uy = HEIGHT/5.0
		dy = -11.0*HEIGHT/21.0
		py = random.randrange(40.0, 160.0)
		self.ay = 2*(py*dy - t*uy)/(py*pow(t,2) - t*pow(py,2))
		self.by = (pow(py,2)*dy - pow(t,2)*uy)/(t*pow(py,2) - py*pow(t,2))
		#dx
		dx = (number*WIDTH/10.0)
		ux = (random.randint(-25, 25)*WIDTH/10.0)
		px = random.randrange(40.0, 160.0)
		self.ax = 2*(px*dx - t*ux)/(px*pow(t,2) - t*pow(px,2))
		self.bx = (pow(px,2)*dx - pow(t,2)*ux)/(t*pow(px,2) - px*pow(t,2))

class camera(spyral.View):
	def __init__(self, Scene, q):
		super(camera, self).__init__(Scene)
		self.lin = Line(self)
		self.lin.pos = (-WIDTH*2.5, 6*HEIGHT/7)
		self.anchor = 'center'
		self.measures = []
		self.measurenumbers = []
		for i in range(51):
			measure = measureLine(self,((i-25)*WIDTH/10.0, 6*HEIGHT/7))
			self.measures.append(measure)
			number = drawFont(self, str(i-25), spyral.Font(FONT, 15, (0,0,0)))
			number.anchor = 'center'
			number.pos = ((i-25)*WIDTH/10.0, 6*HEIGHT/7 + number.height)
			self.measurenumbers.append(number)
		self.nick = Nick(self)
		self.nick.pos = (0, 6*HEIGHT/7)

		self.q = q
		self.balls = []
		ball1 = Ball(self)
		ball1.updateFormula(q.randomNumOne)
		self.balls.append(ball1)
		ball2 = Ball(self)
		ball2.updateFormula(q.randomNumTwo)
		self.balls.append(ball2)

		if q.qtype == "representation":
			ball3 = Ball(self)
			ball3.updateFormula(q.randomNumThree)
			self.balls.append(ball3)

		self.shootOn = False
		self.shoot = 0
		self.edible = True

		self.move = False
		self.linedx = WIDTH/36.0
		spyral.event.register("input.keyboard.down.left", self.left)
		spyral.event.register("input.keyboard.down.right", self.right)
		spyral.event.register("input.keyboard.up.left", self.stop)
		spyral.event.register("input.keyboard.up.right", self.stop)
		spyral.event.register("director.update", self.update)

	def update(self):
		if self.move == "right":
			self.pos = (self.pos[0] - self.linedx, self.pos[1])
		elif self.move == "left":
			self.pos = (self.pos[0] + self.linedx, self.pos[1])
		self.shootBall()
	def stop(self):
		self.move = False

	def left(self):
		self.move = "left"

	def right(self):
		self.move = "right"

	def shootBall(self):
		if self.shoot:
			if not self.shootOn:
				for b in self.balls:
					b.visible = True
					b.pos = (0, HEIGHT/3)
				self.shootOn = True
			for b in self.balls:
				if b.t > int(b.limt - 1):
					break
				elif b.t == int(b.limt - 1):
					b.x = b.number * WIDTH/10.0
					b.edible = False
					b.t += 1
				else:
					b.t += 1
					b.y -= (b.ay*b.t + b.by)
					b.x += (b.ax*b.t + b.bx)

			pass
		pass

class mainScreen(spyral.Scene):
	def __init__(self, q, difficulty):
		super(mainScreen, self).__init__(SIZE)
		model.loadResources()
		self.background = spyral.Image(size=SIZE)
		self.background.fill((255,255,255))
		self.cam = camera(self, q)
		self.cam.pos = (WIDTH/2, self.cam.pos[1])
		self.camy = self.cam.pos[1]
		self.steve = Steve(self)
		self.q = q
		print self.q.randomNumOne
		print self.q.randomNumTwo

		self.countdown = drawFont(self, "Ready!", spyral.Font(FONT,30,(0,0,0)))
		self.countdown.anchor = 'midtop'
		self.countdown.pos = (WIDTH/2, 0)
		self.count = 0

		spyral.event.register("director.update", self.update)

	def update(self):
		if self.steve.body.tempy < HEIGHT/1.7:
			self.steve.body.y = HEIGHT/1.7
			dy = HEIGHT/1.7 - self.steve.body.tempy
			self.cam.y = self.camy + dy
		else:
			self.cam.y = self.camy
			self.steve.body.y = self.steve.body.tempy
		if (self.count < 170):
			self.count += 1
			if (self.count%30 == 0):
				if(self.count < 120):
					self.countdown.update(str(4-self.count/30))
				else:
					self.countdown.update("Start!")
					if self.q.qtype == "compare":
						self.cam.shoot = True
					else:
						self.cam.shoot = 0
		else:
			self.countdown.kill()

		self.steve.update()