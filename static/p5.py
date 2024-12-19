import sys
from pyscript import ffi, js_import
import js

js.eval("""
window.__attach = (name, fn) => window[name] = fn
""")

# These functions should be attached to global scope
_global_functions = """
preload
setup
draw
""".strip().splitlines()

# Just an alias for globalThis
sketch = js

async def init(id):
    locals = sys._getframe(1).f_locals

    for name in _global_functions:
        if name in locals:
            # You must use ffi.create_proxy otherwise the function gets destroyed
            js.__attach(name, ffi.create_proxy(locals[name]))

    # Load p5 library, which will start in global mode because it sees that setup
    # and draw functions are in globalThis
    await js_import('https://cdn.jsdelivr.net/npm/p5@1.11.2/lib/p5.min.js')
