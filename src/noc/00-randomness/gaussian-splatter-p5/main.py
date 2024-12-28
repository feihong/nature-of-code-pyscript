import random
import math
import p5


def setup():
    createCanvas(400, 400)
    background(255)

def draw():
    x = random.gauss(s.width / 2, 60)
    y = random.gauss(s.height / 2, 60)
    c = s.constrain(math.floor(random.gauss(180, 100)), 0, 360)
    noStroke()
    fill(f'hsla({c}, 80%, 50%, 0.2)')
    circle(x, y, 16)

def mousePressed(_event):
    background(255)

p5.init(var='s', id='sketch')
