import sys
from pyscript import document
import js

# These functions should be attached to the instance
_instance_functions = """
draw
mousePressed
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
HSB
HSL
LEFT
MITER
PI
QUARTER_PI
RADIANS
RADIUS
RGB
RIGHT
ROUND
SQUARE
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
loop
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

def init(var, selector=None):
    locals = sys._getframe(1).f_locals

    def callback(instance):
        # Assign value of instance to variable in parent frame
        locals[var] = instance

        for name in _inject_functions:
            locals[name] = getattr(instance, name)

        for name in _instance_functions:
            if name in locals:
                setattr(instance, name, locals[name])

    if selector:
        element = document.querySelector(selector)
    else:
        element = document.createElement('div')
        document.body.appendChild(element)

    return js.p5.new(callback, element)

