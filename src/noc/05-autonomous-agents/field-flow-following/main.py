from pyscript.web import page, p
from p5 import *
from flowfield import FlowField
from vehicle import Vehicle

s = get_instance()

# Use this variable to decide whether to draw the flow field
debug = True

# Flowfield object
flowfield = None
# A list of vehicles
vehicles = None

def setup():
    global flowfield, vehicles

    createCanvas(640, 240)
    # Make a new flow field with "resolution" of 16
    flowfield = FlowField(20)
    # Make a whole bunch of vehicles with random maxspeed and maxforce values
    vehicles = [
        Vehicle(randomUniform(s.width), randomUniform(s.height), randomUniform(2, 5), randomUniform(0.1, 0.5))
        for i in range(120)
    ]

def draw():
    background(255)
    # Display the flowfield if in "debug" mode
    if (debug):
        flowfield.show()
    # Tell all the vehicles to follow the flow field
    for vehicle in vehicles:
        vehicle.follow(flowfield)
        vehicle.run()

def keyPressed(_evt):
    global debug
    if s.key == ' ':
        debug = not debug

# Make a new flowfield
def mousePressed(_evt):
    flowfield.init()

init()

page.append(p('Hit space bar to toggle debugging lines. Click the mouse to generate a new flow field.'))
