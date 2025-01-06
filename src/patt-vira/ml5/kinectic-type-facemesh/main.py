"""
https://editor.p5js.org/codingtrain/sketches/CITZ-7eyA

This sketch runs pretty poorly on Firefox.

"""

from types import SimpleNamespace
import ml5
from p5 import *
s = get_instance()
from letter import Letter

# Values that don't change after setup is run
video = createCapture(VIDEO, flipped=True)
faceMesh = ml5.faceMesh(maxFaces=1, flipped=True)
size = 20
letters = cols = rows = center = None

d = SimpleNamespace(
    face=None,
    mouthX=None,
    mouthY=None,
    mouthW=None,
    angle=0,
    show_video=False,
)

def gotFaces(result, _error):
    d.face = result[0] if result.length > 0 else None

def keyPressed(_evt):
    if s.key == ' ':
        d.show_video = not d.show_video

def setup():
    createCanvas(640, 480)
    video.hide()
    faceMesh.detectStart(video, gotFaces)

    global letters, cols, rows, center
    center = createVector(s.width // 2, s.height // 2)
    Letter.center = center

    cols = s.width // size
    rows = s.height // size

    letters = [[0] * rows for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            x = i * size + size // 2
            y = j * size + size // 2
            letters[i][j] = Letter(x, y, 0.3)

def draw():
    background(0)
    if d.show_video:
        image(video, 0, 0)

    if d.face:
        keypoints = d.face.keypoints
        mouthTop = keypoints[13]
        mouthBottom = keypoints[14]
        fill(255)
        d.mouthX = (mouthTop.x + mouthBottom.x) // 2
        d.mouthY = (mouthTop.y + mouthBottom.y) // 2
        d.mouthW = mouthBottom.y - mouthTop.y
        ellipse(d.mouthX, d.mouthY, 10, 10)

        for keypoint in keypoints:
            fill(255)
            noStroke()
            ellipse(keypoint.x, keypoint.y, 2, 2)

    if d.mouthX is not None:
        center.x = d.mouthX
        center.y = d.mouthY

        fill(255)
        ellipse(center.x, center.y, 10, 10)

        for i in range(cols):
            for j in range(rows):
                if d.mouthW > 30:
                    letters[i][j].scl = 1
                else:
                    if letters[i][j].scl > 0.3:
                        letters[i][j].scl -= 0.01
                    else:
                        letters[i][j].scl = 0.3

                letters[i][j].display(d.angle)

    d.angle += 0.005

init()
