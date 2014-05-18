import spyral
import model
import question
from spyral import Sprite, Vec2D
import math
import random
import model
import copy

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":0, "hard":0}
WHITE = (255,255,255)


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
		self.ate = False
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

	def deRegister(self):
		spyral.event.unregister("input.keyboard.down.space", self.jump)
		spyral.event.unregister("input.keyboard.down.left", self.left)
		spyral.event.unregister("input.keyboard.down.right", self.right)
	def update(self, balls):
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
		if self.ate != False:
			self.ate.pos = (self.head.x + (-WIDTH/35.0 if self.direction == "left" else WIDTH/35.0), self.head.y + WIDTH/50.0)

		if not self.ate:
			for b in balls:
				if(self.body.collide_sprite(b.ball) and b.edible):
					self.ate = Ball(self)
					self.ate.Copyable(b)
					b.visible = False
					break

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
		self.image.draw_lines(WHITE,[(WIDTH/480, 0),(WIDTH/480, HEIGHT/45)],5, False)
		self.pos = pos

class Line(Sprite):
	def __init__(self, View):
		super(Line, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH*5, HEIGHT/180))
		self.anchor = 'topleft'
		self.image.draw_lines(WHITE,[(0, 0),(self.width, 0)],5, False)

class Ball(spyral.View):
	def __init__(self, View):
		super(Ball, self).__init__(View)
		self.ball = Sprite(self)
		self.ball.anchor = 'midbottom'
		self.ball.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.ball.image.draw_circle((random.randint(30,225),random.randint(30,225),random.randint(30,225)),
								(WIDTH/50,WIDTH/50), WIDTH/50, 0, 'topleft')
		self.text = drawFont(self, "",spyral.Font(FONT, WIDTH/40, WHITE))
		self.text.anchor = "midbottom"

		self.text.pos = (self.ball.x, self.ball.y)

		self.number = 0
		self.ay = 0
		self.by = 0
		self.ax = 0
		self.bx = 0
		self.t = 0
		self.limt = 250.0
		self.edible = True		
		self.visible = False

	def Copyable(self, ball):
		self.number = ball.number
		self.visible = True
		self.edible = False
		self.ball.image = ball.ball.image
		self.text.image = ball.text.image

	def updateFormula(self, number):
		self.number = number
		self.text.update(str(number))
		t = self.limt
		#dy
		uy = HEIGHT/5.0
		dy = -11.0*HEIGHT/21.0
		py = random.randrange(40.0, 160.0)
		self.ay = 2*(py*dy - t*uy)/(py*pow(t,2) - t*pow(py,2))
		self.by = (pow(py,2)*dy - pow(t,2)*uy)/(t*pow(py,2) - py*pow(t,2))
		#dx
		dx = (number*WIDTH/10.0)
		ux = (random.randint(-15, 15)*WIDTH/10.0)
		px = random.randrange(40.0, 160.0)
		self.ax = 2*(px*dx - t*ux)/(px*pow(t,2) - t*pow(px,2))
		self.bx = (pow(px,2)*dx - pow(t,2)*ux)/(t*pow(px,2) - px*pow(t,2))

class camera(spyral.View):
	def __init__(self, Scene, q):
		super(camera, self).__init__(Scene)
		self.lin = Line(self)
		self.lin.pos = (-WIDTH*2.5, 6*HEIGHT/7)
		self.anchor = 'center'
		self.balldrop = False
		self.stopScroll = False
		self.measures = []
		self.measurenumbers = []
		for i in range(51):
			measure = measureLine(self,((i-25)*WIDTH/10.0, 6*HEIGHT/7))
			self.measures.append(measure)
			number = drawFont(self, str(i-25), spyral.Font(FONT, 15, WHITE))
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

		self.move = False
		self.linedx = WIDTH/36.0
		spyral.event.register("input.keyboard.down.left", self.left)
		spyral.event.register("input.keyboard.down.right", self.right)
		spyral.event.register("input.keyboard.up.left", self.stop)
		spyral.event.register("input.keyboard.up.right", self.stop)
		spyral.event.register("director.update", self.update)
		self.scrolldirection = "left"

	def scroll(self, number):
		if not self.stopScroll:
			if number * WIDTH/10.0 + WIDTH/2 > self.x:
				self.scrolldirection = "right"
				if number * WIDTH/10.0 + WIDTH/2 <= self.x + self.linedx:
					self.x = number * WIDTH/10.0 + WIDTH/2
					self.stopScroll = True
				else:
					self.x += self.linedx
			elif number * WIDTH/10.0 + WIDTH/2 < self.x:
				if number * WIDTH/10.0 + WIDTH/2 >= self.x - self.linedx:
					self.x = number * WIDTH/10.0 + WIDTH/2
					self.stopScroll = True
				else:
					self.x -= self.linedx

	def deRegister(self):
		spyral.event.unregister("input.keyboard.down.left", self.left)
		spyral.event.unregister("input.keyboard.down.right", self.right)
		spyral.event.unregister("input.keyboard.up.left", self.stop)
		spyral.event.unregister("input.keyboard.up.right", self.stop)

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
		if self.shoot and not self.balldrop:
			if not self.shootOn:
				for b in self.balls:
					b.visible = True
					b.pos = (0, HEIGHT/3)
				self.shootOn = True
			for b in self.balls:
				if b.t > int(b.limt - 1):
					self.balldrop = True
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
		self.background = model.resources["background"]
		self.cam = camera(self, q)
		self.cam.pos = (WIDTH/2, self.cam.pos[1])
		self.camy = self.cam.pos[1]
		self.steve = Steve(self)
		self.q = q
		self.choose = False #for comparison only
		self.correct = False #initial
		self.dreg = False

		print self.q.randomNumOne
		print self.q.randomNumTwo

		self.countdown = drawFont(self, "Ready!", spyral.Font(FONT,WIDTH/30,WHITE))
		self.countdown.anchor = 'midtop'
		self.countdown.pos = (WIDTH/2, 40)
		self.count = 0
		self.hint = drawFont(self, "Hint: Whatever falls on the right is greater", spyral.Font(FONT,WIDTH/40,WHITE))
		self.hint.anchor = 'midbottom'
		self.hint.pos = (WIDTH/2, HEIGHT - 20)
		self.ballimage =[]
		self.ballpointers = []
		ballpointer = drawFont(self, "", spyral.Font(FONT, WIDTH/30, WHITE))
		ballpointer.visible = False
		ballpointer.anchor = 'center'
		self.ballpointers.append(ballpointer)
		self.offtime = 0
		
		if q.qtype == "compare":
			ball2pointer = drawFont(self, "", spyral.Font(FONT, WIDTH/30, WHITE))
			ball2pointer.visible = False
			ball2pointer.anchor = 'center'
			self.ballpointers.append(ball2pointer)
		
		self.selector = drawFont(self, " ", spyral.Font(FONT, WIDTH/120, WHITE))
		self.selector.pos = (WIDTH/2, self.countdown.y + WIDTH/40 + WIDTH/10)
		self.selector.anchor = "center"
		spyral.event.register("director.update", self.update)

	def update(self):
		for i in range(len(self.ballpointers)):
			currentx = -self.cam.x + WIDTH/2
			if self.cam.balls[i].visible and math.fabs(self.cam.balls[i].x - currentx) > WIDTH/2:
				if self.cam.balls[i].x < currentx:
					self.ballpointers[i].update("<= " + str(self.cam.balls[i].number))
					self.ballpointers[i].pos = (self.ballpointers[i].image.width/2,self.cam.balls[i].y)
					self.ballpointers[i].visible = True
				else:
					self.ballpointers[i].update(str(self.cam.balls[i].number) + " =>")
					self.ballpointers[i].pos = (WIDTH-self.ballpointers[i].image.width/2,self.cam.balls[i].y)
					self.ballpointers[i].visible = True
			else:
				self.ballpointers[i].update(" ")
				self.ballpointers[i].visible = False

		if self.steve.body.tempy < HEIGHT/1.7:
			self.steve.body.y = HEIGHT/1.7
			dy = HEIGHT/1.7 - self.steve.body.tempy
			self.cam.y = self.camy + dy
		else:
			self.cam.y = self.camy
			self.steve.body.y = self.steve.body.tempy
		if (self.count < 250):
			self.count += 1
			if (self.count%30 == 0):
				if(self.count < 120):
					self.countdown.update(str(4-self.count/30))
				else:
					if self.q.qtype == "compare":
						if(self.q.comparator == 1):
							self.countdown.update("Go, Steve! Fetch bigger one!")
						else:
							self.countdown.update("Go, Steve! Fetch smaller one!")
						if(not self.cam.shoot):
							self.cam.shoot = True
							i = 1
							for b in self.cam.balls:
								bt = Ball(self)
								bt.ball.image = b.ball.image
								bt.text.image = b.text.image
								bt.text.y += HEIGHT/20
								bt.visible = True
								bt.pos = (i*WIDTH/3, self.countdown.y + WIDTH/40 + WIDTH/10)
								i += 1
								self.ballimage.append(bt)
					else:
						self.cam.shoot = 0
		else:
			self.countdown.kill()
		self.steve.update(self.cam.balls)
		if self.q.qtype == "compare":
			if not self.choose and self.steve.ate != False:
				self.correct = self.steve.ate.number == self.q.answer
				print self.correct
				for i in range(0,2):
					if not self.cam.balls[i].visible:
						selector = math.fabs(self.q.comparator - i)
						self.selector.update(">" if selector > 0 else "<")
						self.choose = True
						break

		if not self.dreg and (self.choose or self.cam.balldrop):
			self.steve.deRegister()
			self.cam.deRegister()
			self.cam.stop()
			self.dreg = True
			eval("self.steve." + self.cam.scrolldirection + "()")
		
		if self.dreg and self.choose and self.cam.balldrop:
			self.cam.scroll(-self.steve.ate.number)

		if self.cam.stopScroll and self.offtime < 100:
			self.offtime += 1

		if self.offtime == 100:
			spyral.director.pop()
			spyral.director.get_scene().submitScreenAnswer(self.correct)
