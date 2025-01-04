# This is a PyScript p5 adaption of
# https://github.com/tabreturn/processing.py-book/tree/master/miscellaneous/digital_aquatics
from p5 import *
s = get_instance()

def setup():
    createCanvas(500, 500)
    generate()
    noLoop()

def generate():
    fillcolor = color(randomUniform(256),
                      randomUniform(256),
                      randomUniform(256),
                      randomUniform(128, 230))

    # remove bubble and bgcolor arguments for a transparent perimeter
    aquatic = Aquatic(s.width/2, s.height/2, randomUniform(80, 130),
                      fillcolor, bubble=True, bgcolor='#D7E1FA')
    aquatic.drawAquatic()

# Press r to regenerate, s to save image
def keyPressed(_evt):
    match s.key:
      case 's':
          filename = f'aquatic-{hour():02}-{minute():02}-{second():02}.png'
          save(filename)
      case 'r':
          loop()
          generate()
          noLoop()

class Aquatic:
    def __init__(self, x, y, size, fillcolor, bubble=False, bgcolor=None):
        # main variables
        self.x = x
        self.y = y
        self.s = size
        self.f = fillcolor
        self.r = red(self.f)
        self.g = green(self.f)
        self.b = blue(self.f)
        self.a = alpha(self.f)
        self.bubble = bubble
        self.bg = bgcolor
        self.eyelist = []
        self.currentx = randomUniform(-self.s/8, self.s/8)
        self.currenty = randomUniform(-self.s/8, self.s/8)
        strokeJoin(ROUND)

    def drawIrisPupil(self, pupilx, pupily, pupilsize):
        s = pupilsize/4 + randomUniform(pupilsize/3)

        # iris
        if randomUniform(1) < 0.7:
            fill(255-self.r, 255-self.g, 255-self.b, self.a/1.5)
            stroke(255-self.r, 255-self.g/2, 255-self.b, 140)
        else:
            fill(self.r*2, self.g, self.b, self.a/2)
            stroke(self.r, self.g/2, self.b, 140)

        strokeWeight(2)
        circle(pupilx, pupily, s*2)

        # pupil
        fill(1)
        stroke(0)
        strokeWeight(5)
        circle(pupilx, pupily, s/2)

    def drawEyeLid(self, eyex, eyey, eyesize):
        fill(self.r, self.g, self.b, randomUniform(200, 240))
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(1)
        arc(eyex, eyey, eyesize*2, eyesize*2, PI, TWO_PI, CHORD)

    def drawEyes(self, eyex, eyey, eyesize):
        stroke(self.r/2, self.g/2, self.b/2, 220)

        # eyelashes
        if randomUniform(1) > .3:
            strokeWeight(2.5)
            translate(eyex, eyey)
            rot = 0

            for eyelash in range(int(randomUniform(3, 8))):
                randomrot = randomUniform(.2, .7)
                rot += randomrot
                rotate(randomrot)
                line(0, 0, randomUniform(-eyesize*2, -eyesize*1.2), 0)

            rotate(-rot)
            translate(-eyex, -eyey)

        # eye
        fill(255)
        strokeWeight(2)
        circle(eyex, eyey, eyesize*2)
        self.drawIrisPupil(eyex, eyey, eyesize)
        # eye shine
        fill(255)
        noStroke()
        shinexy = eyesize/4
        shinesize = eyesize/2.5
        circle(eyex-shinexy, eyey-shinexy, shinesize)

        # eyelid
        if randomUniform(1) > .5:
            self.drawEyeLid(eyex, eyey, eyesize)

    def drawHair(self, hairx, hairy, hairlength, angle):
        tipx = cos(angle) * hairlength
        tipy = sin(angle) * hairlength
        curve(hairx-randomUniform(-100, 100), hairy+randomUniform(-100, 100),
              hairx, hairy,
              tipx+self.currentx, tipy+self.currenty,
              tipx-randomUniform(-100, 100), tipy+randomUniform(-100, 100))

    def superShape(self, m, n1, n2, n3, a, b, radius, start, stop,
                   xoff=0, yoff=0, xdistort=1, cw=True, mode='vertex'):
        # https://en.wikipedia.org/wiki/Superformula
        def superShapeVertex(angle):
            t1 = pow(abs((1.0/a) * cos(angle*m/4)), n2)
            t2 = pow(abs((1.0/b) * sin(angle*m/4)), n3)
            t3 = pow(t1+t2, 1.0/n1)
            x = (t3 * cos(angle) * xdistort * radius) + xoff
            y = (t3 * sin(angle) * radius) + yoff
            return [x, y]

        # plot supershape clock/counter-clockwise
        # drawing hairs only works with cw=True
        angle = start
        tuftstart = randomUniform(0, PI)
        tuftend = randomUniform(PI, TWO_PI)

        if cw:
            while angle < stop:
                xy = superShapeVertex(angle)
                if mode == 'vertex':
                    vertex(xy[0], xy[1])
                elif mode == 'hair':
                    noFill()
                    stroke(self.r/2, self.g/2, self.b/2, 200)
                    strokeWeight(.8)
                    self.drawHair(xy[0], xy[1], radius*randomUniform(1.1, 1.2), angle)
                    if angle > tuftstart and angle < tuftend:
                        strokeWeight(2)
                        hairlength = radius*randomUniform(1.3, 1.5)
                        self.drawHair(xy[0], xy[1], hairlength, angle)
                angle += .05
        else:
            while angle > stop:
                xy = superShapeVertex(angle)
                vertex(xy[0], xy[1])
                angle -= .05

    def drawAquatic(self):
        # outline/mouth variables
        # b_ for body; m_ for mouth
        n1 = (-.8-randomUniform(5) if randomUniform(1) < .5 else .8+randomUniform(5))
        n2 = .5 + randomUniform(5)
        ba = randomUniform(.7, 1.2)
        bb = 1
        bm = int(randomUniform(1, 30))
        bn3 = 1 + randomUniform(-0.3, 0.3) # variation control
        ma = randomUniform(.9, 1.1)
        mb = randomUniform(.9, 1.1)
        mradius = self.s * randomUniform(.2, .4)
        mxoff = self.s / randomUniform(.9, 1.1)

        # bubbles
        if self.bubble:
            noStroke()
            fill(255, 255, 255)
            bs = self.s * 0.8
            circle(self.x+randomUniform(-bs, bs), self.y+randomUniform(-bs, bs), bs)
            circle(self.x+randomUniform(-bs, bs), self.y+randomUniform(-bs, bs), self.s/2)

        # nucleus
        rot = randomUniform(-PI, PI)
        xoff = self.x-self.s/3 * (1 if randomUniform(1) < .5 else -1)
        yoff = self.y+self.s / randomUniform(1.5, 20)
        translate(xoff, yoff)
        rotate(rot)
        fill(self.r/2, self.g/2, self.b/2, 80)
        stroke(self.r/2, self.g/2, self.b/2, 80)
        ellipse(0, 0, self.s/randomUniform(1, 3), self.s/randomUniform(1, 3))
        fill(self.r/3, self.g/3, self.b/3, 120)
        circle(0, 0, self.s/6)
        rotate(-rot)
        translate(-xoff, -yoff)

        # supershapes
        rot = randomUniform(HALF_PI-.3, HALF_PI+.3)
        translate(self.x, self.y)
        rotate(rot)
        # ectoplasm
        noFill()
        stroke(255, 255, 255)
        strokeWeight(self.s/8)
        with shape():
            self.superShape(bm, n1, n2, bn3, ba, bb,
                            self.s-self.s/12, .5, TWO_PI-.5)
        # body
        fill(self.r, self.g, self.b, 120)
        stroke(self.r/2, self.g/2, self.b/2, 220)
        strokeWeight(self.s/12)
        with shape(True):
            self.superShape(bm, n1, n2, bn3, ba, bb, self.s, .5, TWO_PI-.5)
            # mouth
            self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                            xoff=mxoff, xdistort=1.5, cw=False)
        # freckles
        fill(self.r*1.8, self.g*1.8, self.b*1.8, 150)
        noStroke()
        for i in range(10, 200):
            freckx = i/self.s*150 * sin(i*15) + randomUniform(1, 10)
            frecky = i/self.s*150 * cos(i*15) + randomUniform(1, 10)
            dotsize = randomUniform(1, 10)
            circle(freckx, frecky, dotsize)
        # characters
        chars = 's*.~_.)`:;*"-'
        for char in chars:
            fill(self.r/2, self.g/2, self.b/2, 70)
            play = self.s/2
            textSize(randomUniform(play/3, play/1.5))
            text(char, randomUniform(-play, play/2), randomUniform(-play*1.5, play*1.5))
        # background-colored mask
        fill(self.bg)
        noStroke()
        with shape(True):
            vertex(-s.width*2, -s.height*2)
            vertex(-s.width*2, s.height*4)
            vertex(s.width*4, s.height*4)
            vertex(s.width*4, -s.height*2)
            with contour():
                self.superShape(bm, n1, n2, bn3, ba, bb, self.s, .5, TWO_PI-.5)
                self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                                xoff=mxoff, xdistort=1.5, cw=False)
        # lips
        noFill()
        stroke(self.r/2, self.g/2, self.b/2)
        strokeWeight(self.s/12.0)
        with shape():
            self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                            xoff=mxoff, xdistort=1.5, cw=False)
        stroke((self.r + self.g) * .8,
               (self.g + self.b) * .8,
               (self.b + self.r) * .8,
               128)
        strokeWeight(self.s/22.5)
        with shape():
            self.superShape(bm, .98, 3, bn3, ma, mb, mradius, PI+HALF_PI, HALF_PI,
                            xoff=mxoff, xdistort=1.5, cw=False)
        # hairs
        if randomUniform(1) > .3:
            self.superShape(bm, n1, n2, bn3, ba, bb, self.s, .5, TWO_PI-.5,
                            mode='hair')
        rotate(-rot)
        translate(-self.x, -self.y)

        # eye locations
        eyex = self.x-self.s-randomUniform(self.s/10)

        for i in range(3+int(randomUniform(10))):

            if eyex < self.x+self.s-self.s/2:
                eyex = eyex + randomUniform(-10, 10)
                eyex += randomUniform(30, 50)
                eyey = self.y + randomUniform(-self.s/1.5, self.s/5)
                eyesize = 8 + randomUniform(self.s/5.0)

                tup = (eyex, eyey, eyesize)
                self.eyelist.append(tup)

        for eye in self.eyelist:
            self.drawEyes(eye[0], eye[1], eye[2])

init()
