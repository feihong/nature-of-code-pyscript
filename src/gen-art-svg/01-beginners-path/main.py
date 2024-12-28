import random
from pyscript import window, when
from pyscript.web import div
from sv import add_sketch, add_class_sketch, svg, circle, rect, ellipse

@add_sketch('Hilma af Klint-inspired Composition')
def hilma():
    return svg(width=500, height=500, style={'background-color': '#ad3622'}, children=[
        circle(r=125, cy=250, cx=250, fill='#d0d1c9'),
        circle(r=100, cy=250, cx=250, fill='#1c1c1c'),
        circle(r=75, cy=250, cx=250, fill='#5085b4'),
        circle(r=50, cy=250, cx=250, fill='#d6a946'),
    ])

@add_class_sketch
class First:
    title = 'Our first generative sketch'

    def __init__(self):
        self.content = div(self.neonloops(), on_click=lambda _evt: self.regenerate())

        @when('keypress', 'html')
        def keypress(_event): self.regenerate()

    def render(self):
        return div(
            div('Press any key to regenerate'),
            self.content,
        )

    def ellipses(self, hue, rotation, iterations):
        center = 500
        neg_pos = 1 if hue < 180 else -1

        for i in range(iterations):
            yield ellipse(
                cx=center,
                cy=center,
                rx=100 + (i * 3),
                ry=300 + (i * 2),
                fill='none',
                stroke=f'hsla({hue + neg_pos * (i * 3)}, 80%, 80%, 0.6)',
                transform=f'rotate({rotation + (i * 2)} {center} {center})')

    def neonloops(self):
        size = window.innerWidth if window.innerWidth < window.innerHeight else window.innerHeight
        hue = random.randint(0, 360)
        rotation = random.randint(-180, 180)
        iterations = random.randint(10, 100)

        return svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
            rect(x=0, y=0, width=1000, height=1000, fill='#181818'),
            *self.ellipses(hue, rotation, iterations),
        ])

    def regenerate(self):
        self.content.innerHTML = ''
        self.content.append(self.neonloops())
