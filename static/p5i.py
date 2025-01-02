from pyscript import document, ffi
import js

# We need to use this helper function because trying to set functions on the p5 instance directly from Python results in
# odd race conditions
js.eval("""
function _createP5Instance(obj, element) {
  const callback = (sketch) => {
    for (const [name, fn] of Object.entries(obj)) {
      sketch[name] = () => fn(sketch)
    }
  }
  return new p5(callback, element)
}
""")

# These functions should be attached to the p5 instance
_instance_functions = """
preload
setup
draw
""".strip().splitlines()

def add_sketch(cls):
    if hasattr(cls, 'title'):
        title = cls.title if cls.title is not None else cls.__name__
        h2 = document.createElement('h2')
        h2.textContent = title
        document.body.appendChild(h2)

    if selector := getattr(cls, 'selector', None):
        element = document.querySelector(selector)
    else:
        element = document.createElement('div')
        document.body.appendChild(element)

    instance_funcs = {}
    for name in _instance_functions:
        if fn := getattr(cls, name, None):
            instance_funcs[name] = fn

    _p5_instance = js._createP5Instance(ffi.to_js(instance_funcs), element)
    return cls
