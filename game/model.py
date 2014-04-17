from hero import Hero
from card import Card

class Model:
    allCards = [Card("Math")]

    def initHero(self, name):
        self.hero = Hero(name)
