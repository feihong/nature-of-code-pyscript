import sys
from pyscript import ffi
import js

js.eval("""
function createQ5Instance(id) {
  // Use instance mode: https://github.com/q5js/q5.js/wiki/Instance-Mode
  const instance = new Q5('instance', document.getElementById(id))
  instance._attach = (name, fn) => {
     instance[name] = fn
  }
  return instance
}
""")

# These functions should be attached to the q5 instance
_instance_functions = """
preload
setup
draw
""".strip().splitlines()

def init(id):
    locals = sys._getframe(1).f_locals
    instance = js.createQ5Instance(id)

    for name in _instance_functions:
        if name in locals:
            # Need to use ffi.create_proxy or else the proxy object is destroyed
            instance._attach(name, ffi.create_proxy(locals[name]))

    return instance
