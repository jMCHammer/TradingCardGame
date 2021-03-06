import spyral
import model
import question
from spyral import Sprite, Vec2D
import math
import random

FONT = "Extras/Comic_Book.ttf"
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
DIFFICULTY = {"easy":0, "medium":1, "hard":1}
WHITE = (255,255,255)

# If you don't know what I am doing... just tell me what to do. (= v=)

class drawFont(Sprite):
	def __init__(self, Scene, text, font):
		super(drawFont,self).__init__(Scene)
		self.f = font
		self.text = text
		self.image = self.f.render(self.text)

	def update(self, string):
		self.text = string
		self.image = self.f.render(self.text)

class Particle(spyral.View):
	def __init__(self, View, num):
		super(Particle, self).__init__(View)
		self.num = num
		self.ratiobot = 10.0
		self.ratio = self.num/self.ratiobot
		self.layers = ['circle','font']

		self.part = Sprite(self)
		self.part.anchor = 'center'
		self.part.layer = 'circle'
		self.part.image = spyral.Image(size=((3*WIDTH/12.0), (3*WIDTH/12.0)))
		self.radius = int(self.ratio*(3*WIDTH/48))
		self.part.image.draw_circle((120,120,120),
				((3*WIDTH/24.0),(3*WIDTH/24.0)),
				self.radius,0,'topleft')

		self.numtext = drawFont(self, str(num) if num != 0 else '', spyral.Font(FONT, 30, WHITE))
		self.numtext.pos = self.part.pos
		self.numtext.anchor = 'center'
		self.numtext.layer = 'font'

	def numUpdate(self,num,merging):
		self.num = num
		if(merging):
			self.ratiobot = pow(10.0, len(str(num)) - 2)
		else:
			crack = crackingNum(self, -self.scene.scene.hammer.number)
			crack.pos = self.numtext.pos
		self.ratio = self.num/self.ratiobot
		self.part.image = spyral.Image(size=((3*WIDTH/12.0), (3*WIDTH/12.0)))
		self.radius = int(self.ratio*(3*WIDTH/48))
		self.part.image.draw_circle((120,120,120),
				((3*WIDTH/24.0),(3*WIDTH/24.0)),
				self.radius,0,'topleft')
		self.numtext.update(str(int(num)) if num != 0 else '')
		self.numtext.pos = self.part.pos

class crackingNum(drawFont):
	def __init__(self, View, num):
		super(crackingNum, self).__init__(View, str(num), spyral.Font(FONT, 30, (255,0,0)))
		self.time = 40.0
		xdist = random.choice(range(-WIDTH/12,-1) + range(1,WIDTH/12))
		he = WIDTH/120.0
		self.layer = 'top'
		self.t = 0
		self.a = 8.0*he/(pow(2*xdist/3.0,2))
		self.b = 4.0*he/(2*xdist/3.0)
		self.w = xdist/self.time
		spyral.event.register("director.update", self.update)

	def update(self):
		if(self.t > self.time):
			spyral.event.unregister("director.update", self.update)
			self.kill()
		else:
			self.t += 1
			dy = self.a*math.fabs(self.w)*self.t + self.b
			self.x += self.w
			self.y += dy

class measureLine(Sprite):
	def __init__(self, View, pos):
		super(measureLine, self).__init__(View)
		self.image = spyral.Image(size=(WIDTH/240.0, HEIGHT/30.0))
		self.anchor = 'center'
		self.image.draw_lines(WHITE,[(WIDTH/480, 0),(WIDTH/480, HEIGHT/30.0)],5, False)
		self.pos = pos

class ironBoard(spyral.View):
	def __init__(self, View, diff, denominator):
		super(ironBoard, self).__init__(View)
		self.layers = ['bottom','top']
		self.board = Sprite(self)
		self.board.image = spyral.Image(size = (3*WIDTH/2.0, HEIGHT/30.0))
		self.board.image.draw_rect((120,120,120),(0,0),(3*WIDTH/2.0,HEIGHT/30.0),0,'topleft')
		self.board.layer = 'bottom'
		self.anchor = 'midleft'
		self.measures = []
		self.particles = []
		self.diff = DIFFICULTY[diff]

		self.numHam = [0,0,0,0,0]

		#change the number into string...without dot		
		self.denom = ''
		point = False #did you find the decimal point?
		d = 0 #location of the decimal point
		for c in str(denominator*10 if self.scene.q.randomNumOne%1 > 0 else denominator):
			if(c != '.'):
				self.denom += c
				if not point:
					d += 1
			else:
				point = True

		if len(self.denom) < 5:
			self.denom = '0' * (5-len(self.denom)) + self.denom
			d += 5-len(self.denom)

		print self.denom
		#initialize measure lines
		for i in range(0,6):
			measure = measureLine(self, (i * 3*WIDTH/10.0,HEIGHT/60.0))
			measure.layer = 'top'
			self.measures.append(measure)

		#initialize particle
		for i in range(0, 5):
			pn = int(self.denom[i])
			particle = Particle(self,pn)
			particle.pos = (i * 3*WIDTH/10.0 + 3*WIDTH/16.0,HEIGHT/360.0 - particle.radius)
			self.particles.append(particle)

		spyral.event.register("director.update", self.update)
		spyral.event.register("input.keyboard.down.right", self.scroll)

		self.currentParticle = 0

		self.scrol = False
		self.dist = 3*WIDTH/10.0
		self.time = 30.0
		self.tick = 0.0
		self.dx = self.dist/self.time
		self.currentPlate = 0

	def killView(self):
		spyral.event.unregister("director.update", self.update)
		spyral.event.unregister("input.keyboard.down.right", self.scroll)

	def update(self):
		if self.scrol and self.currentPlate < 5:
			if(self.time > self.tick):
				self.x -= self.dx
				self.particles[self.currentParticle].x += self.dx
				self.tick += 1
			else:
				self.scrol = False
				self.tick = 0.0
				n = self.particles[self.currentParticle].num
				if self.currentParticle < len(self.particles) - 1:
					self.particles[self.currentParticle].kill()
				self.currentParticle += 1
				if len(self.particles) > self.currentParticle:
					self.particles[self.currentParticle].numUpdate(n * 10.0 + self.particles[self.currentParticle].num, True)
					self.particles[self.currentParticle].y = HEIGHT/360.0 - self.particles[self.currentParticle].radius
				self.currentPlate += 1
		if self.currentPlate >= 5:
			self.killView()
			self.scene.isWin(False)

	def scroll(self):
		if not self.scrol and not self.scene.hammer.hammertime:
			self.scrol = True
		pass

class ironHammer(spyral.View):
	def __init__(self, Scene, divisor):
		super(ironHammer, self).__init__(Scene)
		self.layers = ['hammer', 'weight']
		self.head = Sprite(self)
		self.head.image = model.resources["hammer"]
		self.head.anchor = 'topleft'
		self.head.pos = (WIDTH/10 - WIDTH/12, HEIGHT/10 - 100)
		self.head.layer = 'hammer'
		self.isBroke = False

		self.anchor = "bottomleft"

		if divisor%1 > 0.0:
			self.number = int(divisor * 10)
		else:
			self.number = int(divisor)

		wt = drawFont(self, str(self.number), spyral.Font(FONT, 50, (255,255,255)))
		wt.anchor = 'center'
		wt.layer = 'weight'
		wt.pos = (self.head.x + WIDTH/3.0 - 75, self.head.y + HEIGHT/8.0)

		self.hammertime = False
		self.tick = 0.0
		self.t = 20.0
		self.p = 3.0
		self.h = 2*HEIGHT/4.0 - HEIGHT/4.5

		spyral.event.register("director.update", self.update)
		spyral.event.register("input.keyboard.down.down", self.hammerTime)

	def killView(self):
		spyral.event.unregister("director.update", self.update)
		spyral.event.unregister("input.keyboard.down.down", self.hammerTime)

	def update(self):
		if self.hammertime:
			if self.tick < self.p:
				self.y += self.h/self.p
			elif self.tick < self.t and not self.isBroke:
				self.y -= self.h/(self.t - self.p)
			else:
				self.hammertime = False
				self.tick = -1.0
			if self.tick == self.p:
				particle = self.scene.board.particles[self.scene.board.currentParticle]
				if particle.num >= self.number and not self.isBroke:
					particle.numUpdate(particle.num - self.number, False)
					particle.y = HEIGHT/360.0 - particle.radius
					numHam = self.scene.board.numHam
					at = self.scene.board.currentPlate
					if(numHam[at] >= 9):
						self.isBroke = True
						self.killView()
						self.scene.board.killView()
						self.scene.isWin(True)
						pass # TODO: failcase implementation
					else:
						numHam[at] += 1
						self.scene.numHam[at].update(str(numHam[at]))
				else:
					self.isBroke = True
					self.killView()
					self.scene.board.killView()
					self.scene.isWin(True)
					pass # TODO: failcase implementation
			self.tick += 1

	def hammerTime(self):
		if not self.hammertime and not self.scene.board.scrol and (self.scene.board.currentPlate < 5):
			self.hammertime = True

class mainScreen(spyral.Scene):
    def __init__(self, q, diff):
        super(mainScreen, self).__init__(SIZE)
        model.loadResources()
        self.background = model.resources["background"]
        self.layers = ['bot', 't']
        self.q = q
        print str(q.answer) + ' ' + str(q.randomNumOne) + ' ' + str(q.randomNumTwo)
        self.answer = q.answer
        self.board = ironBoard(self,diff, q.randomNumTwo)
        self.board.pos = (WIDTH/4,3*HEIGHT/4.0)
        self.hammer = ironHammer(self, q.randomNumOne)
        self.hammer.pos = (WIDTH/7.5,HEIGHT/4.5)
        self.correct = False

        text1 = drawFont(self, "Use the hammer to crush the numbers that can", spyral.Font(FONT, 30, WHITE))
        text1.pos = (WIDTH/2, 0)
        text1.anchor = 'midtop'
        text2 = drawFont(self, "be divided by the number on the hammer!", spyral.Font(FONT, 30, WHITE))
        text2.pos = (WIDTH/2, text1.height + 10)
        text2.anchor = 'midtop'
        text3 = drawFont(self, "Answer: ", spyral.Font(FONT, 30, WHITE))
        text3.pos = (WIDTH/2 - 100, HEIGHT - 50)
        text3.anchor = 'midbottom'
        
        idkwhatthefuckamidoing = 1 if q.randomNumTwo % 1 > 0 else 0
        dividend = drawFont(self, "Dividend: " + str(int(self.board.denom)/pow(10.0,idkwhatthefuckamidoing)), spyral.Font(FONT, 30, WHITE))
        dividend.pos = (WIDTH/2, HEIGHT - 80)
        dividend.anchor = 'midbottom'

        helpText = drawFont(self, "Right Arrow: Move Right     Down Arrow: Hammer Time", spyral.Font(FONT, 30, WHITE))
        helpText.pos = (WIDTH/2, HEIGHT - 10)
        helpText.anchor = 'midbottom'

        self.numHam = []

        for i in range(1,6):
            numham = drawFont(self, '', spyral.Font(FONT, 30, (255,255,255)))
            numham.anchor = 'midbottom'
            numham.pos = (WIDTH/3 + 50 + (i * WIDTH/20.0), HEIGHT - 50)
            numham.layer = 't'
            self.numHam.append(numham)
        if self.answer%1 > 0:
            dot = drawFont(self, '.', spyral.Font(FONT, 30, (255,255,255)))
            dot.pos = (WIDTH/3 + 50 + (4.5 * WIDTH/20.0), HEIGHT - 50)
            dot.anchor = 'midbottom'
            dot.layer = 't'

        #Scene pop wait time
        self.popwait = 50
        self.popt = 0

    def wait(self):
        if(self.popt < self.popwait):
            self.popt += 1
        else:
            spyral.event.unregister("director.update", self.wait)
            print "end main screen"
            spyral.director.pop()
            spyral.director.get_scene().submitScreenAnswer(self.correct)
            pass
		#TODO make transition from mainScreen to resultScreen

    def isWin(self, fail):
        if fail:
            resultText = drawFont(self, "Incorrect.  Answer is " + str(self.answer), spyral.Font(FONT, 50, (255,0,0)))
            resultText.pos = (WIDTH/2, HEIGHT/3)
            resultText.anchor = 'center'
            pass
        else:
            answer = 0
            answerline = self.board.numHam
            if self.answer%1 > 0:
                isdot = 1
            else:
                isdot = 0
                self.answer = int(self.answer)

            for i in range(0,5):
                answer += answerline[i] * pow(10, 4 - i - isdot)

            print answer
            self.correct = self.answer == answer
            resultText = drawFont(self, "Correct!", spyral.Font(FONT, 50, (0,255,0)))
            resultText.pos = (WIDTH/2 + 200, HEIGHT/3)
            resultText.anchor = 'center'
        spyral.event.register("director.update", self.wait)