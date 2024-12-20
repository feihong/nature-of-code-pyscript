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
    instance = js.Q5.new('instance', pyscript.document.getElementById(id))

    # Assign value of instance to variable in parent frame
    locals[var] = instance

    for name in _inject_functions:
        locals[name] = getattr(instance, name)

    for name in _instance_functions:
        if name in locals:
            setattr(instance, name, locals[name])

    return instance
