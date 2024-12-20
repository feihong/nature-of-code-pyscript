import random
import p5

def setup():
    createCanvas(400, 400)
    background(255)

def draw():
    x = random.gauss(s.width / 2, 60)
    y = random.gauss(s.height / 2, 60)
    noStroke()
    fill(0, 10)
    circle(x, y, 16)

def mousePressed(_event):
    background(255)

p5.init(var='s', id='sketch')
