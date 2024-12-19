import random
import q5

def setup():
    createCanvas(640, 240)
    background(255)

def draw():
    x = random.gauss(320, 60)
    noStroke()
    fill(0, 10)
    circle(x, 120, 16)

s = q5.init('sketch')
from q5 import *
