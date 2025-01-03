import random
import p5

class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        match random.randint(0, 3):
            case 0:
                self.x += 1
            case 1:
                self.x -= 1
            case 2:
                self.y += 1
            case _:
                self.y -= 1

walker = Walker()

def setup():
    createCanvas(640, 240)
    background(245)
    walker.x = s.width / 2
    walker.y = s.height / 2

def draw():
    walker.step()
    walker.show()

p5.init(var='s')
