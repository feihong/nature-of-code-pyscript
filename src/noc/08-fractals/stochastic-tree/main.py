from p5 import *
s = get_instance()

# Perlin noise offset
yoff = 0
# Random seed to control randomness while drawing the tree
seed = 5

def setup():
    createCanvas(360, 240)

def draw():
    global yoff
    background(255)
    fill(0)

    stroke(0)
    # Start the tree from the bottom of the screen
    translate(s.width / 2, s.height)
    # Move along through noise
    yoff += 0.005
    randomSeed(seed)
    # Start the recursive branching!
    branch(60, 0)

def branch(h, xoff):
    # Thickness of the branch is mapped to its length
    sw = remap(h, 2, 100, 1, 5)
    strokeWeight(sw)
    # Draw the branch
    line(0, 0, 0, -h)
    # Move along to end
    translate(0, -h)

    # Each branch will be 2/3rds the size of the previous one
    h *= 0.7

    # Move along through noise space
    xoff += 0.1

    if h > 4:
        # Random number of branches
        n = floor(randomUniform(1, 5))
        for i in range(n):
            # Here the angle is controlled by perlin noise
            # This is a totally arbitrary way to do it, try others!
            theta = remap(noise(xoff + i, yoff), 0, 1, -PI/2, PI/2)
            if n % 2 == 0:
                theta *= -1

            with push():          # Save the current state of transformation (i.e. where are we now)
                rotate(theta)     # Rotate by theta
                branch(h, xoff)   # Ok, now call myself to branch again

def mousePressed(_evt):
    global yoff, seed
    # New tree starts with new noise offset and new random seed
    yoff = randomUniform(1000)
    seed = millis()

init()
