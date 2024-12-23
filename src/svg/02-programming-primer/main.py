import itertools
import math
from pyscript import window
from pyscript.web import page, h2
from sv import svg, rect, circle, g

def circles():
    steps = ['00', '33', '66', '99', 'CC', 'FF']
    web_safe_colors = (f'#'+r+g+b for r,g,b in itertools.product(steps, repeat=3))

    angle = 0
    radius = 5
    increment = (math.pi * 12) / (len(steps) ** 3)

    for i, web_safe_color in enumerate(web_safe_colors):
        angle = increment * i
        yield circle(
            cx=math.cos(angle) * radius,
            cy=math.sin(angle) * radius,
            r=1 + (i / 20.),
            transform='translate(500, 500)',
            fill=web_safe_color)
        radius += 2

size = window.innerWidth if window.innerWidth < window.innerHeight else window.innerHeight

sketch = page.find('#sketch')[0]
sketch.append(
    h2('Web-safe color spiral'),
    svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
        rect(x=0, y=0, width=1000, height=1000, fill='#181818'),
        g(*circles())
    ])
)
