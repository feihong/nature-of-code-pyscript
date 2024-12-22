from pyscript import document, when
from pyscript.web import page, div, select, option
import q5

get_choice = lambda: document.location.hash[1:].replace('%20', ' ')

def setup():
    if get_choice() == 'robot':
        resizeCanvas(720, 480)
    else:
        resizeCanvas(480, 120)

def draw():
    background(204)

    match get_choice():
        case 'line':
            line(20, 50, 420, 110)
        case 'shapes':
            quad(158, 55, 199, 14, 392, 66, 351, 107)
            triangle(347, 54, 392, 9, 392, 66)
            triangle(158, 55, 290, 91, 290, 112)
        case 'rectangle':
            rect(180, 60, 220, 40)
        case 'ellipse':
            ellipse(278, -100, 400, 400)
            ellipse(120, 100, 110, 110)
            ellipse(412, 60, 18, 18)
        case 'arc':
            arc(90, 60, 80, 80, 0, HALF_PI)
            arc(190, 60, 80, 80, 0, PI+HALF_PI)
            arc(290, 60, 80, 80, PI, TWO_PI+HALF_PI)
            arc(390, 60, 80, 80, QUARTER_PI, PI+QUARTER_PI)
        case 'angleMode':
            angleMode(DEGREES)
            arc(90, 60, 80, 80, 0, 90)
            arc(190, 60, 80, 80, 0, 270)
            arc(290, 60, 80, 80, 180, 450)
            arc(390, 60, 80, 80, 45, 225)
            angleMode(RADIANS)
        case 'strokeWeight':
            ellipse(75, 60, 90, 90)
            strokeWeight(8)   # Stroke weight to 8 pixels
            ellipse(175, 60, 90, 90)
            ellipse(279, 60, 90, 90)
            strokeWeight(20)  # Stroke weight to 20 pixels
            ellipse(389, 60, 90, 90)

            strokeWeight(1)
        case 'strokeJoin strokeCap':
            strokeWeight(12)
            strokeJoin(ROUND)      # Round the stroke corners
            rect(40, 25, 70, 70)
            strokeJoin(BEVEL)      # Bevel the stroke corners
            rect(140, 25, 70, 70)
            strokeCap(SQUARE)      # Square the line endings
            line(270, 25, 340, 95)
            strokeCap(ROUND)       # Round the line endings
            line(350, 25, 420, 95)

            strokeWeight(1)
        case 'grays':
            background(0)                # Black
            fill(204)                    # Light gray
            ellipse(132, 82, 200, 200)   # Light gray circle
            fill(153)                    # Medium gray
            ellipse(228, -16, 200, 200)  # Medium gray circle
            fill(102)                    # Dark gray
            ellipse(268, 118, 200, 200)  # Dark gray circle

            fill(0)
        case 'noFill noStroke':
            fill(153)                    # Medium gray
            ellipse(132, 82, 200, 200)   # Gray circle
            noFill()                     # Turn off fill
            ellipse(228, -16, 200, 200)  # Outline circle
            noStroke()                   # Turn off stroke
            ellipse(268, 118, 200, 200)  # Doesn’t draw!

            fill(0)
            stroke(0)
        case 'color':
            background(40, 50, 100)        # Dark blue color
            fill(255, 0, 0)              # Red color
            ellipse(132, 82, 200, 200)   # Red circle
            fill(0, 255, 0)              # Green color
            ellipse(228, -16, 200, 200)  # Green circle
            fill(0, 0, 255)              # Blue color
            ellipse(268, 118, 200, 200)  # Blue circle

            fill(0)
        case 'transparency':
            noStroke()
            background(204, 226, 225)    # Light blue color
            fill(255, 0, 0, 160)         # Red color
            ellipse(132, 82, 200, 200)   # Red circle
            fill(0, 255, 0, 160)         # Green color
            ellipse(228, -16, 200, 200)  # Green circle
            fill(0, 0, 255, 160)         # Blue color
            ellipse(268, 118, 200, 200)  # Blue circle

            fill(0)
            stroke(0)
        case 'arrow':
            beginShape()
            vertex(180, 82)
            vertex(207, 36)
            vertex(214, 63)
            vertex(407, 11)
            vertex(412, 30)
            vertex(219, 82)
            vertex(226, 109)
            endShape(CLOSE)
        case 'creatures':
            # Left creature
            fill(255)
            beginShape()
            vertex(50, 120)
            vertex(100, 90)
            vertex(110, 60)
            vertex(80, 20)
            vertex(210, 60)
            vertex(160, 80)
            vertex(200, 90)
            vertex(140, 100)
            vertex(130, 120)
            endShape()
            fill(0)
            ellipse(155, 60, 8, 8)

            # Right creature
            fill(255)
            beginShape()
            vertex(370, 120)
            vertex(360, 90)
            vertex(290, 80)
            vertex(340, 70)
            vertex(280, 50)
            vertex(420, 10)
            vertex(390, 50)
            vertex(410, 90)
            vertex(460, 120)
            endShape()
            fill(0)
            ellipse(345, 50, 10, 10)
        case 'robot':
            strokeWeight(2)
            ellipseMode(RADIUS)

            # Neck
            stroke(102)                # Set stroke to gray
            line(266, 257, 266, 162)   # Left
            line(276, 257, 276, 162)   # Middle
            line(286, 257, 286, 162)   # Right

            # Antennae
            line(276, 155, 246, 112)   # Small
            line(276, 155, 306, 56)    # Tall
            line(276, 155, 342, 170)   # Medium

            # Body
            noStroke()                 # Disable stroke
            fill(102)                  # Set fill to gray
            ellipse(264, 377, 33, 33)  # Antigravity orb
            fill(0)                    # Set fill to black
            rect(219, 257, 90, 120)    # Main body
            fill(102)                  # Set fill to gray
            rect(219, 274, 90, 6)      # Gray stripe

            # Head
            fill(0)                    # Set fill to black
            ellipse(276, 155, 45, 45)  # Head
            fill(255)                  # Set fill to white
            ellipse(288, 150, 14, 14)  # Large eye
            fill(0)                    # Set fill to black
            ellipse(288, 150, 3, 3)    # Pupil
            fill(153)                  # Set fill to light gray
            ellipse(263, 148, 5, 5)    # Small eye 1
            ellipse(296, 130, 4, 4)    # Small eye 2
            ellipse(305, 162, 3, 3)    # Small eye 3

            # Reset
            fill(0)
            stroke(0)
            strokeWeight(1)
            ellipseMode(CENTER)
        case _:
          textAlign(CENTER, CENTER)
          textSize(40)
          text('你好世界！', s.width / 2, s.height / 2)

q5.init(var='s', id='sketch')

sketch = page.find('#sketch')[0]
choices = ('hello|line|shapes|rectangle|ellipse|arc|angleMode|strokeWeight|strokeJoin strokeCap|grays|noFill noStroke'
  '|color|transparency|arrow|creatures|robot').split('|')
sketch.append(
   div(
      select(id='choices', *(option(s, value=s, selected=get_choice()==s) for s in choices))
   )
)

@when('change', '#choices')
def change(event):
    new_choice = event.target.value
    document.location.hash = '#' + new_choice
    if new_choice == 'robot':
        resizeCanvas(720, 480)
    else:
        resizeCanvas(480, 120)
