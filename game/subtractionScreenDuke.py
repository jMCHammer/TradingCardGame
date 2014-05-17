import spyral
from spyral import Sprite
import question
import math
import model

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
FONT = "Extras/Comic_Book.ttf"
DIFFICULTY = {"easy":0, "medium":1, "hard":1}
WHITE = (255, 255, 255)

class drawFont(Sprite):
    def __init__(self, Scene, text, font):
        super(drawFont,self).__init__(Scene)
        self.f = font
        self.text = text
        self.image = self.f.render(self.text)

    def update(self, string):
        self.text = string
        self.image = self.f.render(self.text)

class Person(Sprite):
	def __init__(self, Scene, pos):
		super(Person, self).__init__(Scene)
		self.pos = pos
		self.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.circlePosition = (WIDTH/50,WIDTH/50)
		self.anchor = 'center'
		self.color = (0,0,0)
		pass

class Borrower(Person):
	def __init__(self, Scene, diff):
		super(Borrower, self).__init__(Scene, (0,0))
		self.diff = diff
		self.color = (171, 31, 206)
		self.image.draw_circle(self.color, self.circlePosition, WIDTH/50, 0,'topleft')
		self.position = 1
		self.dx = WIDTH/(3 + DIFFICULTY[diff])
		self.x = self.position * self.dx
		self.y = HEIGHT/8

		spyral.event.register("input.keyboard.down.left", self.moveLeft)
		spyral.event.register("input.keyboard.down.right", self.moveRight)
		spyral.event.register("director.update", self.Update)

	def moveLeft(self):
		if(self.position > 1):
			self.position -= 1

	def moveRight(self):
		if(self.position < 2 + DIFFICULTY[self.diff]):
			self.position += 1

	def Update(self):
		self.x = self.position * self.dx

class Pebble(Sprite):
	def __init__(self, Scene, colord):
		super(Pebble, self).__init__(Scene)
		self.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.circlePosition = (WIDTH/50,WIDTH/50)
		self.anchor = 'center'
		self.color = colord
		self.digit = 0
		self.image.draw_circle(self.color, self.circlePosition, WIDTH/50, 0,'topleft')

class dyingPebble(Sprite):
	def __init__(self, Scene, colord, height, pos, dist):
		super(dyingPebble, self).__init__(Scene)
		self.pos = pos
		self.h = height
#		self.h = (height - self.y)/50.0
		self.dist = (self.x - dist + WIDTH/50)/2
		self.w = -self.dist/25.0
		self.image = spyral.Image(size=(WIDTH/25, WIDTH/25))
		self.circlePosition = (WIDTH/50,WIDTH/50)
		self.anchor = 'center'
		self.color = colord
		self.image.draw_circle(self.color, self.circlePosition, WIDTH/50, 0,'topleft')
		spyral.event.register("director.update", self.Update)
		self.ty = 0
		self.tx = 0
		self.died = False

	def Update(self):
		if(self.y > 2*HEIGHT/3 + WIDTH/25):
			self.died = True
		elif(self.ty >= 0):
			dy = (0.245*WIDTH/1200.0)*self.ty
			if(self.y + dy > self.h - HEIGHT/50):
				self.y = self.h - HEIGHT/50
				self.ty = -1
			else:
				self.y += dy
				self.ty += 1
		elif(self.tx < 25):
			he = WIDTH/6.0
			a = 8*he/(float(pow(self.dist,2)))
			b = 4*he/float(self.dist)
			self.tx += 1
			self.x += self.w
			dy = a*self.w*self.tx + b
			if(self.y - dy > self.h):
				self.y = self.h - HEIGHT/50
			else:
				self.y -= dy
		else:
			he = WIDTH/9
			a = 8*he/(float(pow(self.dist,2)))
			b = 4*he/float(self.dist)
			self.tx += 1
			self.x += self.w
			self.y -= a*self.w*(self.tx-25) + b
		if self.died:
			self.kill()

class LegitBeaker(Sprite):
    def __init__(self, Scene):
        super(LegitBeaker, self).__init__(Scene)
        self.image = model.resources['beaker']

class Beaker(Sprite):
	def __init__(self, Scene, diff):
		super(Beaker, self).__init__(Scene)
		self.image = spyral.Image(size=(WIDTH/(4+DIFFICULTY[diff]),HEIGHT/50))
		self.color = (180,180,200)
		self.diff = diff
		self.image.draw_rect(self.color,(WIDTH/1000, 0),(WIDTH/(4+DIFFICULTY[diff]) - WIDTH/500, HEIGHT/50), 0, 'center')

	def fillup(self):
		self.color = (80,80,127)
		self.image.draw_rect(self.color,(WIDTH/1000, 0),(WIDTH/(4+DIFFICULTY[self.diff]) - WIDTH/500, HEIGHT/50), 0, 'center')

class mainScene(spyral.Scene):
    def __init__(self, q, diff):
        super(mainScene, self).__init__(SIZE)
        model.loadResources();
        self.background = model.resources["background"]
        self.diff = diff        
        self.answer = q.answer
        self.firstnum = max(q.randomNumOne, q.randomNumTwo)
        self.secondnum = min(q.randomNumOne, q.randomNumTwo)
        self.borrower = Borrower(self, diff)
        self.deakers = []
        self.subFrom = []
        self.subBy = []
        self.filllist = [0,0,0]
        self.text1 = drawFont(self,"We need the perfect mixture to fuel us to victory!", spyral.Font(FONT, 25, WHITE))
        self.text2 = drawFont(self,"We have " + str(self.firstnum) + " pebbles but we only need " + str(self.secondnum) +"! Place the difference back in the beakers!", spyral.Font(FONT, 25, WHITE))
        self.text3 = drawFont(self,"Fill in the beakers but do not overflow them!",spyral.Font(FONT,25,WHITE))
        self.text4 = drawFont(self,"Down: Fill up the beaker       Space : Lend the pebble to the right", spyral.Font(FONT,25,WHITE))
        self.text1.pos = (WIDTH/6 + 25, 0)
        self.text2.pos = (25, self.text1.height + self.text1.pos.y)		
        self.text3.pos = (WIDTH/5 + 25, self.text2.height + self.text2.pos.y)
        self.text4.pos = (WIDTH/9, HEIGHT - 30)
        spyral.event.register("input.keyboard.down.return", self.submit)

		#initiallize pebbles on subfrom side...
        self.firstnum = int(self.firstnum * 10)
        numString = str(self.firstnum)
        if(DIFFICULTY[diff]>0):
			decimal1 = Pebble(self, (0,0,0))
			decx = self.borrower.dx * 2.5 
			decy = HEIGHT/3 + WIDTH/25
			decimal1.pos = (decx, decy)
        for d in range(1,4):
			subfroms = []
			if(len(numString) >= d):
				n = int(numString[-1*d])
				for i in range(n):
					number = Pebble(self, (78*d,27*d,5*d))
					number.digit = d - 2
					x = self.borrower.dx * (4 - d)
					y = HEIGHT/3
					if i < 4:	
						x += (1.5 - i)*WIDTH/25
						y += WIDTH/25
					elif i < 7:
						x += (5 - i)*WIDTH/25
					elif i < 9:
						x += (7.5 - i)*WIDTH/25
						y -= WIDTH/25
					else:
						y -= 2*WIDTH/25
					number.pos = (x,y)
					subfroms.append(number)
			self.subFrom.append(subfroms)

		#initialize beakers on subby side...
        self.secondnum = int(self.secondnum * 10)
        numString = str(self.secondnum)
        if(DIFFICULTY[diff]>0):
            decimal2 = Pebble(self, (0,0,0))
            decx = self.borrower.dx * 2.5 
            decy = 2*HEIGHT/3 + WIDTH/25
            decimal2.pos = (decx, decy)
        for d in range(1,4):
            subbys = []
            if(len(numString) >= d):
                lbeaker = LegitBeaker(self)
                lbeaker.x = self.borrower.dx * (4 - d) - (lbeaker.width/2)
                lbeaker.y = 1.75*HEIGHT/3 + WIDTH/25
                self.deakers.append(lbeaker)
                n = int(numString[-1*d])
                for i in range(n):
                    beaker = Beaker(self, diff)
                    x = self.borrower.dx * (4 - d) - (beaker.width/2)
                    y = 2*HEIGHT/3 + WIDTH/25 - (beaker.height * i)
                    beaker.pos = (x, y)
                    beaker.visible = False
                    subbys.append(beaker)
            self.subBy.append(subbys)

		#set keyboard control...
        spyral.event.register("input.keyboard.down.down", self.downPebble)
        spyral.event.register("input.keyboard.down.space", self.borrowFrom)

        pass

    def downPebble(self):
		position = len(self.subFrom) - self.borrower.position
		subposition = self.borrower.position -1
		if(len(self.subFrom) > position):
			if(len(self.subFrom[position]) > 0):
				pebble = self.subFrom[position].pop()
				if(len(self.subBy) > position):
					if(len(self.subBy[position]) > self.filllist[subposition]):
						self.subBy[position][self.filllist[subposition]].fillup()
					else:
						downpebble = dyingPebble(self, pebble.color, 
							2*HEIGHT/3 + WIDTH/25 - (HEIGHT/50 * len(self.subBy[position])),
							(self.borrower.x, HEIGHT/3 + 2*WIDTH/25),
							self.borrower.x - WIDTH/(2*(4+DIFFICULTY[self.diff])))
				pebble.kill()
				self.filllist[subposition] += 1

    def borrowFrom(self):
		position = len(self.subFrom) - self.borrower.position
		if(len(self.subFrom) > position and position > 0):
			if(len(self.subFrom[position-1]) == 0):
				self.subFrom[position].pop().kill()
				subfroms = []
				d = position
				for i in range(10):
					number = Pebble(self, (78*d,27*d,5*d))
					number.digit = d - 2
					x = self.borrower.dx * (4 - d)
					y = HEIGHT/3
					if i < 4:	
						x += (1.5 - i)*WIDTH/25
						y += WIDTH/25
					elif i < 7:
						x += (5 - i)*WIDTH/25
					elif i < 9:
						x += (7.5 - i)*WIDTH/25
						y -= WIDTH/25
					else:
						y -= 2*WIDTH/25
					number.pos = (x,y)
					subfroms.append(number)
				self.subFrom[position-1] = subfroms

    def submit(self):
		submission = 0.0
		for i in range(3):
			submission += len(self.subFrom[2-i]) * pow(10,1-i)
		correct = int(submission*10) == int(self.answer*10)
		spyral.director.pop()
		spyral.director.get_scene().submitScreenAnswer(correct)
