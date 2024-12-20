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
background
circle
createCanvas
fill
noStroke
point
rect
stroke
""".strip().splitlines()

def init(var, id):
    locals = sys._getframe(1).f_locals

    def callback(instance):
        # Assign value of instance to variable in parent frame
        locals[var] = instance

        for name in _inject_functions:
            locals[name] = getattr(instance, name)

        for name in _instance_functions:
            if name in locals:
                setattr(instance, name, locals[name])

    return js.p5.new(callback, document.getElementById(id))

