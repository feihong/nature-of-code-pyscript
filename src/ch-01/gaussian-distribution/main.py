import random
import q5

def setup():
    s.createCanvas(640, 240)
    s.background(255)

def draw():
    x = random.gauss(320, 60)
    s.noStroke()
    s.fill(0, 10)
    s.circle(x, 120, 16)

s = q5.init('sketch')
