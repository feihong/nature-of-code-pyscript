import random
import types
from pyscript import when
from pyscript.web import page, span, div, input_
import q5

v = types.SimpleNamespace(x_mu=0, y_mu=0, xy_sigma=60, color_sigma=100)

def setup():
    createCanvas(400, 400)
    background(255)
    colorMode(OKLCH)
    v.x_mu = s.width / 2
    v.y_mu = s.height / 2

def draw():
    x = random.gauss(v.x_mu, v.xy_sigma)
    y = random.gauss(v.y_mu, v.xy_sigma)
    c = random.gauss(180, v.color_sigma)
    noStroke()
    fill(0.7, 0.3, c, 0.4)
    circle(x, y, 16)

    if s.mouseIsPressed:
        v.x_mu = s.mouseX
        v.y_mu = s.mouseY
        background(1, 0, 0)

q5.init(var='s', id='sketch')

# sliders to adjust standard deviation values
sketch = page.find('#sketch')[0]
sketch.append(
    div(
        div(
            'xy stddev:',
            div(str(v.xy_sigma), classes='xy-label'),
            input_(classes='xy-slider', type='range', min='0', max='200', step='1', value=str(v.xy_sigma)),
            style={'display': 'flex', 'gap': '8px'},
        ),
        div(
            'color stddev:',
            div(str(v.color_sigma), classes='color-label'),
            input_(classes='color-slider', type='range', min='0', max='180', step='1', value=str(v.color_sigma)),
            style={'display': 'flex', 'gap': '8px'},
        ),
    )
)

@when('change', 'input.xy-slider')
def change(evt):
    v.xy_sigma = int(evt.target.value)
    page.find('div.xy-label').textContent = evt.target.value

@when('change', 'input.color-slider')
def change(evt):
    v.color_sigma = int(evt.target.value)
    page.find('div.color-label').textContent = evt.target.value
