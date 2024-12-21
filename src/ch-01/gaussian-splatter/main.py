import random
import q5

def setup():
    createCanvas(400, 400)
    background(255)
    colorMode(OKLCH)

def draw():
    x = random.gauss(s.width / 2, 60)
    y = random.gauss(s.height / 2, 60)
    c = random.gauss(180, 180)
    noStroke()
    fill(0.7, 0.3, c, 0.4)
    circle(x, y, 16)

    if s.mouseIsPressed:
        background(1, 0, 0)

q5.init(var='s', id='sketch')
