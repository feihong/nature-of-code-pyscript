import sys
import js
import pyscript

# These functions should be attached to the q5 instance
_instance_functions = """
draw
preload
setup
""".strip().splitlines()

# These functions will be injected into the parent frame
_inject_functions = """
BASELINE
BEVEL
BOTTOM
CENTER
CLOSE
CORNER
CORNERS
DEGREES
HALF_PI
LEFT
MITER
OKLCH
PI
QUARTER_PI
RADIANS
RADIUS
RGB
RIGHT
ROUND
SQUARE
SRGB
TOP
TWO_PI
angleMode
arc
background
beginShape
circle
colorMode
createCanvas
ellipse
ellipseMode
endShape
fill
line
noFill
noLoop
noStroke
point
quad
radians
rect
resizeCanvas
stroke
strokeCap
strokeJoin
strokeWeight
text
textAlign
textSize
triangle
vertex
""".strip().splitlines()

def init(var, id):
    locals = sys._getframe(1).f_locals
    instance = js.Q5.new('instance', pyscript.document.getElementById(id))

    # Assign value of instance to variable in parent frame
    locals[var] = instance

    for name in _inject_functions:
        locals[name] = getattr(instance, name)

    for name in _instance_functions:
        if name in locals:
            setattr(instance, name, locals[name])

    return instance
