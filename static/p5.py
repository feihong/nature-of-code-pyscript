import sys
from pyscript import document, ffi
import js

# These functions should be attached to the instance
_instance_functions = """
mousePressed
""".strip().splitlines()

# These values will be copied into this module
_inject_values = """
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

for name in _inject_values:
    vars()[name] = getattr(js._p5Instance, name)

_p5_element = None

def createCanvas(*args):
    canvas = js._p5Instance.createCanvas(*args)
    canvas.parent(_p5_element)
    canvas.show() # have to show it explicitly because it's initially hidden

def get_instance():
    return js._p5Instance

def init(selector=None):
    global _p5_element

    if selector:
        _p5_element = document.querySelector(selector)
    else:
        _p5_element = document.createElement('div')
        document.body.appendChild(_p5_element)

    locals = sys._getframe(1).f_locals

    for name in _instance_functions:
        if name in locals:
            setattr(js._p5Instance, name, locals[name])

    draw_functions = [locals[name] for name in ('preload', 'setup', 'draw') if name in locals]
    js._p5Instance._init(ffi.to_js(draw_functions))
