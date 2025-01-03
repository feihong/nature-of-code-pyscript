import random
import p5

def setup():
    createCanvas(640, 240)
    background(255)

def draw():
    x = random.gauss(320, 60)
    noStroke()
    fill(0, 10)
    circle(x, 120, 16)

p5.init(var='s')
