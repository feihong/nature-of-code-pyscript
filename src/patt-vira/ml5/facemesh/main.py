import ml5
from p5 import *
s = get_instance()

video = createCapture(VIDEO, flipped=True)
faceMesh = ml5.faceMesh(maxFaces=3, flipped=True)
faces = []

def gotFaces(results, _error):
    global faces
    faces = results

def setup():
    createCanvas(640, 480)

    video.hide()
    faceMesh.detectStart(video, gotFaces)

    print(ml5.version)

def mousePressed(_event):
    print(faces)

def draw():
    background(0)
    image(video, 0, 0)

    for face in faces:
        lips = face.lips
        strokeWeight(4)
        noFill()
        stroke(255, 100, 255)
        rect(lips.x, lips.y, lips.width, lips.height)

        for lipPoint in lips.keypoints:
            strokeWeight(2)
            stroke(0, 255, 0)
            point(lipPoint.x, lipPoint.y)

init()
