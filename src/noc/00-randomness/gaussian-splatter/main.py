import random
import math
from pyscript.web import page, p
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

p5.init(var='s')

page.append(p('Exercise 0.4: Consider a simulation of paint splatter drawn as a collection of colored dots. Most of the paint clusters around a central position, but some dots splatter out toward the edges. Can you use a normal distribution of random numbers to generate the positions of the dots? Can you also use a normal distribution of random numbers to generate a color palette? Try creating a slider to adjust the standard deviation.'))
