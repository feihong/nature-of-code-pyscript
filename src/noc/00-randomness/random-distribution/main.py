import random
from p5 import *
s = get_instance()

total = 20
random_counts = [0 for _ in range(total)]

def setup():
    createCanvas(640, 240)

def draw():
    background(255)

    index = random.randrange(0, total)
    random_counts[index] += 1

    stroke(0)
    fill(127)

    w = s.width / total
    for i in range(total):
        h = random_counts[i]
        rect(i * w, s.height - h, w - 1, h)

init()
