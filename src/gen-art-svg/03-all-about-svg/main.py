from pyscript import window
from pyscript.web import page, link
from sv import add_sketch, svg, circle, rect, text, defs, pattern

size = window.innerWidth if window.innerWidth < window.innerHeight else window.innerHeight
background = lambda: rect(x=0, y=0, width=1000, height=1000, fill='#181818')

@add_sketch('Rectangle color illusion')
def sketch():
  return svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
      background(),
      # Main orange square
      rect(x=150, y=200, width=700, height=600, rx=15, fill='#e56411', stroke='#fff', stroke_width=30,
           paint_order='stroke'),
      # Blue rectangle
      rect(x=650, y=200, width=200, height=600, rx=15, fill='#69969f'),
      # Smaller orange rectangle
      rect(x=200, y=425, width=600, height=150, rx=20, fill='#b84b08'),
      # Yellow rectangle
      rect(x=325, y=200, width=175, height=600, fill='#fed322'),
      # Purple rectangle
      rect(x=500, y=200, width=175, height=600, fill='#49283c'),
  ])

@add_sketch('Circle overlay loop')
def sketch():
  def circles():
    for i in range(1, 7):
      r = 50 * i
      # blueish circle set
      yield circle(cx=500, cy=800 - r, r=r, fill='#99eeff', fill_opacity=0.1)
      # greenish circle set
      yield circle(cx=500, cy=200 + r, r=r, fill='#aaffee', fill_opacity=0.1)

  return svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
      background(),
      *circles(),
      circle(cx=500, cy=500, r=320, fill='none', stroke='#aaffee', stroke_width=2, stroke_opacity=0.1),
  ])

@add_sketch('Chalkboard gag')
def sketch():
  page.head.append(
    link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Mynerve&display=swap')
  )
  line = '"Bart Bucks" are not legal tender.'.upper()
  return svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
      background(),
      *(text(line, x=20, y=80 + i, fill='#fff', font_size=52, font_family='Mynerve') for i in range(0, 960, 80)),
  ])

@add_sketch('Optical illusion')
def sketch():
  def pattern_rects():
    # Create 4 white squares within the pattern.
    for i in range(4):
      yield rect(
        x=20 if i == 3 else i * 20,
        y=i * 50,
        width=50,
        height=50,
        fill='#eee',
      )

    # Create 4 thin grey rectangles to separate the squares.
    for i in range(4):
      yield rect(
        x=0,
        y=45 + i * 50,
        width=100,
        height=5,
        fill='#666',
      )

  return svg(width=size, height=size, viewBox='0 0 1000 1000', children=[
      background(),
      defs(
        pattern(*pattern_rects(), id='illusion', x=0, y=0, width=100, height=200, patternUnits='userSpaceOnUse')
      ),
      rect(x=0, y=0, width=1000, height=1000, fill='url(#illusion)'),
  ])
