import spyral
from spyral import Sprite
from spyral import Vec2D
import random
import math

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class tcg(spyral.scene):
    def __init__(self):
        self.background = spyral.Image(size = SIZE)
