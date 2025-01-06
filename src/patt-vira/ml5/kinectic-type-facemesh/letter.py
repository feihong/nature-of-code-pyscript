from p5 import *

class Letter:
    center = None

    def __init__(self, x, y, scl):
        self.pos = createVector(x, y)
        self.scl = scl

    def display(self, angle):
        self.calcVel(Letter.center, self.pos)
        self.shift = remap(self.distance, 0, 1000, 10, 0)
        self.osc = sin(TWO_PI * angle + self.shift)

        self.fontS = remap(self.osc, -1, 1, 0.3, 1.5)
        with push():
            translate(self.pos.x + self.vel.x * self.osc, self.pos.y + self.vel.y * self.osc)
            fill(255)
            # ellipse(0, 0, 10, 10)
            scale(self.fontS)
            textAlign(CENTER, CENTER)
            text("A", 0, 0)

    def calcAngle(self):
        return atan2(Letter.center.y - self.pos.y, Letter.center.x - self.pos.x) - PI

    def calcVel(self, center, pos):
        angle = self.calcAngle()
        self.vel = Vector.fromAngle(angle)
        self.distance = dist(center.x, center.y, pos.x, pos.y)
        self.vel.setMag(self.distance * self.scl)
        # line(center.x, center.y, center.x + self.vel.x, center.y + self.vel.y)
