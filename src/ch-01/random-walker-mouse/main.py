import random
import q5

class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0

    def show(self):
        s.stroke(0)
        s.point(self.x, self.y)

    def step(self):
        v = random.randrange(0, 100)
        if v < 70:
            self.random_step()
        else:
            self.follow_mouse()

    def random_step(self):
        match random.randint(0, 3):
            case 0:
                self.x += 1
            case 1:
                self.x -= 1
            case 2:
                self.y += 1
            case _:
                self.y -= 1

    def follow_mouse(self):
        match random.choice(['x', 'y']):
            case 'x':
                if s.mouseX - self.x < 0:
                    self.x -= 1
                else:
                    self.x += 1
            case 'y':
                if s.mouseY - self.y < 0:
                    self.y -= 1
                else:
                    self.y += 1

walker = Walker()

def setup():
    s.createCanvas(640, 240)
    s.background(245)
    walker.x = s.width / 2
    walker.y = s.height / 2

def draw():
    walker.step()
    walker.show()

s = q5.init('sketch')