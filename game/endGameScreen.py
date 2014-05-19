import spyral
import random
import model
import math

from card import Card
from spyral import Vec2D
from hero import Hero

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class drawWinFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
        spyral.Sprite.__init__(self,Scene)
        f = spyral.Font(font, 150, WHITE)
        self.image = f.render(text)

class drawTextFont(spyral.Sprite):
    def __init__(self, Scene, font, text):
	    spyral.Sprite.__init__(self, Scene)
	    f = spyral.Font(font, 50, WHITE)
	    self.image = f.render(text)

class drawButton(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.image = spyral.image.Image("Extras/continueButton.png")
        self.pos = (WIDTH/2.6, HEIGHT*9/10)
        spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.pop()

class EndGameScreen(spyral.Scene):
    def __init__(self):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.hero = Hero(self.scene)
        self.background = model.resources["background"]
        if model.opponentDead == True:
            card_guts = model.prizeCard()
            if not card_guts[0] in model.deck and not card_guts[0] in model.looseCards:
                model.looseCards[card_guts[0]] = card_guts
            print card_guts[0]

            card = (Card(self, card_guts[0], card_guts[1], card_guts[2]))
            card.pos = (WIDTH/3, HEIGHT/3)

            winText = drawWinFont(self.scene, "Extras/Comic_Book.ttf", "You win!")
            wincard = drawTextFont(self.scene, "Extras/Comic_Book.ttf", "You've won a card!")
            wincard.pos = (WIDTH/4, 200)
        else:
            winText = drawWinFont(self.scene, "Extras/Comic_Book.ttf", "You lose.")
        winText.pos = (WIDTH/4, 10)

        returnButton = drawButton(self.scene)		

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
