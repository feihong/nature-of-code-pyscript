import sys
from contextlib import contextmanager
from pyscript import document, ffi
import js

# These functions should be attached to the instance
_instance_functions = """
keyPressed
mousePressed
""".strip().splitlines()

# These values will be copied into this module
_inject_values = """
BASELINE
BEVEL
BOTTOM
CENTER
CHORD
CLOSE
CORNER
CORNERS
DEGREES
HALF_PI
HSB
HSL
LEFT
MITER
OPEN
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
alpha
angleMode
arc
background
blue
ceil
circle
color
colorMode
constrain
cos
createVector
curve
ellipse
ellipseMode
fill
floor
green
hour
line
loop
millis
minute
noFill
noise
noiseSeed
noLoop
noStroke
point
quad
radians
randomSeed
rect
red
resizeCanvas
rotate
save
second
sin
stroke
strokeCap
strokeJoin
strokeWeight
text
textAlign
textSize
translate
triangle
vertex
""".strip().splitlines()

js.eval("""
window._p5Instance = new p5(sketch => {
  sketch.setup = () => {
    const canvas = sketch.createCanvas()
    canvas.hide()
    sketch.noLoop()
  }

  sketch._init = (drawFunctions) => {
    const drawAll = () => {
      if (drawFunctions.length > 1) {
        sketch.draw = () => {
          const fn = drawFunctions.shift()
          fn()
          sketch.noLoop()
        }
        sketch.loop()
        setInterval(drawAll, 0)
      } else {
        sketch.draw = drawFunctions[0]
        sketch.loop()
      }
    }
    drawAll()
  }
})
""")

_element = None  # parent element of p5 canvas
_instance = js._p5Instance

for name in _inject_values:
    vars()[name] = getattr(_instance, name)

def createCanvas(*args):
    canvas = _instance.createCanvas(*args)
    canvas.parent(_element)
    canvas.show() # have to show it explicitly because it's initially hidden

# Context manager functions:

@contextmanager
def push():
    _instance.push()
    yield None
    _instance.pop()

@contextmanager
def contour():
    _instance.beginContour()
    yield None
    _instance.endContour()

@contextmanager
def shape(closed=False):
    _instance.beginShape()
    yield None
    _instance.endShape()

@contextmanager
def closedShape():
    _instance.beginShape()
    yield None
    _instance.endShape(_instance.CLOSE)

# Renamed functions:
remap = _instance.map
randomUniform = _instance.random

# Classes:
Vector = js.p5.Vector

def get_instance():
    return _instance

def init(selector=None):
    global _element

    if selector:
        _element = document.querySelector(selector)
    else:
        _element = document.createElement('div')
        document.body.appendChild(_element)

    locals = sys._getframe(1).f_locals

    for name in _instance_functions:
        if name in locals:
            setattr(_instance, name, locals[name])

    draw_functions = [locals[name] for name in ('preload', 'setup', 'draw') if name in locals]
    _instance._init(ffi.to_js(draw_functions))
