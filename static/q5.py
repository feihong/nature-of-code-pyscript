import sys
import js
import pyscript

# These functions should be attached to the q5 instance
_instance_functions = """
draw
preload
setup
""".strip().splitlines()

# These functions will be injected into this module
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

def init(id):
    locals = sys._getframe(1).f_locals
    instance = js.Q5.new('instance', pyscript.document.getElementById(id))

    for name in _instance_functions:
        if name in locals:
            # Need to use ffi.create_proxy or else the proxy object is destroyed
            setattr(instance, name, (locals[name]))

    current_module = sys.modules[__name__]
    for name in _inject_functions:
        setattr(current_module, name, getattr(instance, name))

    return instance
