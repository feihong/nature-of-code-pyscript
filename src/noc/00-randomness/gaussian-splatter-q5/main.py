import random
import types
from pyscript import when
from pyscript.web import page, p, div, input_
import q5

v = types.SimpleNamespace(x_mu=0, y_mu=0, xy_sigma=60, color_sigma=100)

def setup():
    createCanvas(400, 400)
    background(255)
    v.x_mu = s.width / 2
    v.y_mu = s.height / 2

def draw():
    x = random.gauss(v.x_mu, v.xy_sigma)
    y = random.gauss(v.y_mu, v.xy_sigma)
    c = random.gauss(180, v.color_sigma)
    noStroke()
    colorMode(OKLCH)
    fill(0.7, 0.3, c, 0.4)
    circle(x, y, 16)

    if s.mouseIsPressed:
        v.x_mu = s.mouseX
        v.y_mu = s.mouseY
        colorMode(RGB)
        background(255)

q5.init(var='s')

# sliders to adjust standard deviation values
page.append(
    div(
        div(
            'xy stddev:',
            div(str(v.xy_sigma), id='xy-label'),
            input_(id='xy-slider', type='range', min='0', max='200', step='1', value=str(v.xy_sigma)),
            style={'display': 'flex', 'gap': '8px'},
        ),
        div(
            'color stddev:',
            div(str(v.color_sigma), id='color-label'),
            input_(id='color-slider', type='range', min='0', max='180', step='1', value=str(v.color_sigma)),
            style={'display': 'flex', 'gap': '8px'},
        ),
        p('Exercise 0.4: Consider a simulation of paint splatter drawn as a collection of colored dots. Most of the paint clusters around a central position, but some dots splatter out toward the edges. Can you use a normal distribution of random numbers to generate the positions of the dots? Can you also use a normal distribution of random numbers to generate a color palette? Try creating a slider to adjust the standard deviation.'),
    )
)

@when('change', '#xy-slider')
def change(evt):
    v.xy_sigma = int(evt.target.value)
    page.find('#xy-label').textContent = evt.target.value

@when('change', '#color-slider')
def change(evt):
    v.color_sigma = int(evt.target.value)
    page.find('#color-label').textContent = evt.target.value
