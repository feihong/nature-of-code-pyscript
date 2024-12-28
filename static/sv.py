import contextlib
from pyscript import document
from pyscript.web import Element, Classes, Style, page, h2, div

class SvgElement(Element):
    def __init__(self, dom_element=None, classes=None, style=None, **kwargs):
        """Create a new, or wrap an existing DOM element.

        If `dom_element` is None we are being called to *create* a new element.
        Otherwise, we are being called to *wrap* an existing DOM element.
        """
        tag_name = type(self).get_tag_name()
        self._dom_element = dom_element or document.createElementNS('http://www.w3.org/2000/svg', tag_name)

        if tag_name == 'svg':
            setattr(self._dom_element, 'xmlns', 'http://www.w3.org/2000/svg')

        # HTML on_events attached to the element become pyscript.Event instances.
        self._on_events = {}

        # Handle kwargs for handling named events with a default handler function.
        properties = {}
        for name, handler in kwargs.items():
            if name.startswith("on_"):
                ev = self.get_event(name)  # Create the default Event instance.
                ev.add_listener(handler)
            else:
                properties[name] = handler

        # A set-like interface to the element's `classList`.
        self._classes = Classes(self)

        # A dict-like interface to the element's `style` attribute.
        self._style = Style(self)

        # Set any specified classes, styles, and DOM properties.
        self.update(classes=classes, style=style, **properties)

    def __setattr__(self, name, value):
        # This class overrides `__setattr__` to delegate "public" attributes to the
        # underlying DOM element. BUT, we don't use the usual Python pattern where
        # we set attributes on the element itself via `self.__dict__` as that is not
        # yet supported in our build of MicroPython. Instead, we handle it here by
        # using super for all "private" attributes (those starting with an underscore).
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            # This allows us to set attributes on the underlying DOM element that clash
            # with Python keywords or built-ins (e.g. the output element has an
            # attribute `for` which is a Python keyword, so you can access it on the
            # Element instance via `for_`).
            if name.endswith("_"):
                name = name[:-1]

            if name.startswith("on_"):
                # Ensure on-events are cached in the _on_events dict if the
                # user is setting them directly.
                self._on_events[name] = value

            self._dom_element.setAttributeNS(None, name, value)

class SvgContainerElement(SvgElement):
    """Base class for SVG elements that can contain other elements."""

    def __init__(
        self, *args, children=None, dom_element=None, style=None, classes=None, **kwargs
    ):
        super().__init__(
            dom_element=dom_element, style=style, classes=classes, **kwargs
        )

        for child in list(args) + (children or []):
            if isinstance(child, Element) or isinstance(child, ElementCollection):
                self.append(child)
            else:
                self._dom_element.insertAdjacentHTML("beforeend", child)

    def __iter__(self):
        yield from self.children


class svg(SvgContainerElement):
  """Ref: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg"""

class circle(SvgElement):
  """Ref: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle"""

class rect(SvgElement):
  """Ref: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect"""

class ellipse(SvgElement):
  """Ref: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/ellipse"""

class g(SvgContainerElement):
  """Ref: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g"""

def add_sketch(title, selector=None):
    def decorator(func):
        element = page.find(selector)[0] if selector else page
        element.append(h2(title), func())
        return func

    return decorator

def add_class_sketch(cls):
    element = page.find(cls.selector)[0] if hasattr(cls, 'selector') else page
    sketch = cls()
    element.append(h2(cls.title), sketch.render())
    return cls
