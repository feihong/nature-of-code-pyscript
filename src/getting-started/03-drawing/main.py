from pyscript.web import page, h2, div
from p5i import add_sketch

@add_sketch
class line:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)

    def draw(s):
        s.line(20, 50, 420, 110)
        s.noLoop()

@add_sketch
class shapes:
    title = 'quad and triangle'

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.quad(158, 55, 199, 14, 392, 66, 351, 107)
        s.triangle(347, 54, 392, 9, 392, 66)
        s.triangle(158, 55, 290, 91, 290, 112)
        s.noLoop()

@add_sketch
class rect:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.rect(180, 60, 220, 40)
        s.noLoop()

@add_sketch
class ellipse:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.ellipse(278, -100, 400, 400)
        s.ellipse(120, 100, 110, 110)
        s.ellipse(412, 60, 18, 18)
        s.noLoop()

@add_sketch
class arc:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.arc(90, 60, 80, 80, 0, s.HALF_PI)
        s.arc(190, 60, 80, 80, 0, s.PI + s.HALF_PI)
        s.arc(290, 60, 80, 80, s.PI, s.TWO_PI + s.HALF_PI)
        s.arc(390, 60, 80, 80, s.QUARTER_PI, s.PI + s.QUARTER_PI)
        s.noLoop()

@add_sketch
class angleMode:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.angleMode(s.DEGREES)
        s.arc(90, 60, 80, 80, 0, 90)
        s.arc(190, 60, 80, 80, 0, 270)
        s.arc(290, 60, 80, 80, 180, 450)
        s.arc(390, 60, 80, 80, 45, 225)
        s.noLoop()

@add_sketch
class strokeWeight:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.ellipse(75, 60, 90, 90)
        s.strokeWeight(8)   # Stroke weight to 8 pixels
        s.ellipse(175, 60, 90, 90)
        s.ellipse(279, 60, 90, 90)
        s.strokeWeight(20)  # Stroke weight to 20 pixels
        s.ellipse(389, 60, 90, 90)
        s.noLoop()

@add_sketch
class strokeJoin:
    title = 'strokeJoin and strokeCap'

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.strokeWeight(12)
        s.strokeJoin(s.ROUND)      # Round the stroke corners
        s.rect(40, 25, 70, 70)
        s.strokeJoin(s.BEVEL)      # Bevel the stroke corners
        s.rect(140, 25, 70, 70)
        s.strokeCap(s.SQUARE)      # Square the line endings
        s.line(270, 25, 340, 95)
        s.strokeCap(s.ROUND)       # Round the line endings
        s.line(350, 25, 420, 95)
        s.noLoop()

@add_sketch
class grays:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(0)                # Black
        s.fill(204)                    # Light gray
        s.ellipse(132, 82, 200, 200)   # Light gray circle
        s.fill(153)                    # Medium gray
        s.ellipse(228, -16, 200, 200)  # Medium gray circle
        s.fill(102)                    # Dark gray
        s.ellipse(268, 118, 200, 200)  # Dark gray circle
        s.noLoop()

@add_sketch
class noFill:
    title = 'noFill and noStroke'

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.fill(153)                    # Medium gray
        s.ellipse(132, 82, 200, 200)   # Gray circle
        s.noFill()                     # Turn off fill
        s.ellipse(228, -16, 200, 200)  # Outline circle
        s.noStroke()                   # Turn off stroke
        s.ellipse(268, 118, 200, 200)  # Doesn’t draw!
        s.noLoop()

@add_sketch
class color:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(40, 50, 100)        # Dark blue color
        s.fill(255, 0, 0)              # Red color
        s.ellipse(132, 82, 200, 200)   # Red circle
        s.fill(0, 255, 0)              # Green color
        s.ellipse(228, -16, 200, 200)  # Green circle
        s.fill(0, 0, 255)              # Blue color
        s.ellipse(268, 118, 200, 200)  # Blue circle
        s.noLoop()

@add_sketch
class transparency:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.noStroke()
        s.background(204, 226, 225)    # Light blue color
        s.fill(255, 0, 0, 160)         # Red color
        s.ellipse(132, 82, 200, 200)   # Red circle
        s.fill(0, 255, 0, 160)         # Green color
        s.ellipse(228, -16, 200, 200)  # Green circle
        s.fill(0, 0, 255, 160)         # Blue color
        s.ellipse(268, 118, 200, 200)  # Blue circle
        s.noLoop()

@add_sketch
class arrow:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        s.beginShape()
        s.vertex(180, 82)
        s.vertex(207, 36)
        s.vertex(214, 63)
        s.vertex(407, 11)
        s.vertex(412, 30)
        s.vertex(219, 82)
        s.vertex(226, 109)
        s.endShape(s.CLOSE)
        s.noLoop()

@add_sketch
class creatures:
    title = None

    def setup(s):
        s.createCanvas(480, 120)
        s.background(204)
        # Left creature
        s.fill(255)
        s.beginShape()
        s.vertex(50, 120)
        s.vertex(100, 90)
        s.vertex(110, 60)
        s.vertex(80, 20)
        s.vertex(210, 60)
        s.vertex(160, 80)
        s.vertex(200, 90)
        s.vertex(140, 100)
        s.vertex(130, 120)
        s.endShape()
        s.fill(0)
        s.ellipse(155, 60, 8, 8)

        # Right creature
        s.fill(255)
        s.beginShape()
        s.vertex(370, 120)
        s.vertex(360, 90)
        s.vertex(290, 80)
        s.vertex(340, 70)
        s.vertex(280, 50)
        s.vertex(420, 10)
        s.vertex(390, 50)
        s.vertex(410, 90)
        s.vertex(460, 120)
        s.endShape()
        s.fill(0)
        s.ellipse(345, 50, 10, 10)
        s.noLoop()

@add_sketch
class robot:
    title = None

    def setup(s):
        s.createCanvas(720, 480)
        s.background(204)
        s.strokeWeight(2)
        s.ellipseMode(s.RADIUS)

        # Neck
        s.stroke(102)                # Set stroke to gray
        s.line(266, 257, 266, 162)   # Left
        s.line(276, 257, 276, 162)   # Middle
        s.line(286, 257, 286, 162)   # Right

        # Antennae
        s.line(276, 155, 246, 112)   # Small
        s.line(276, 155, 306, 56)    # Tall
        s.line(276, 155, 342, 170)   # Medium

        # Body
        s.noStroke()                 # Disable stroke
        s.fill(102)                  # Set fill to gray
        s.ellipse(264, 377, 33, 33)  # Antigravity orb
        s.fill(0)                    # Set fill to black
        s.rect(219, 257, 90, 120)    # Main body
        s.fill(102)                  # Set fill to gray
        s.rect(219, 274, 90, 6)      # Gray stripe

        # Head
        s.fill(0)                    # Set fill to black
        s.ellipse(276, 155, 45, 45)  # Head
        s.fill(255)                  # Set fill to white
        s.ellipse(288, 150, 14, 14)  # Large eye
        s.fill(0)                    # Set fill to black
        s.ellipse(288, 150, 3, 3)    # Pupil
        s.fill(153)                  # Set fill to light gray
        s.ellipse(263, 148, 5, 5)    # Small eye 1
        s.ellipse(296, 130, 4, 4)    # Small eye 2
        s.ellipse(305, 162, 3, 3)    # Small eye 3
        s.noLoop()
