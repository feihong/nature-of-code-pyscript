from p5 import *
s = get_instance()

class FlowField:
    def __init__(self, r):
        self.resolution = r
        # {!2} Determine the number of columns and rows.
        self.cols = s.width // self.resolution
        self.rows = s.height // self.resolution
        # {!4} A flow field is a two-dimensional list of vectors. The example includes a separate function to create that array.
        self.field = [[0]*self.rows for _ in range(self.cols)]
        self.init()

    # The init() function fills the 2D list with vectors
    def init(self):
        # Reseed noise for a new flow field each time
        noiseSeed(randomUniform(10000))
        xoff = 0;
        for i in range(self.cols):
            yoff = 0;
            for j in range(self.rows):
                # {.code-wide} In this example, use Perlin noise to create the vectors.
                angle = remap(noise(xoff, yoff), 0, 1, 0, TWO_PI)
                self.field[i][j] = Vector.fromAngle(angle)
                yoff += 0.1

            xoff += 0.1

    # Draw every vector
    def show(self):
        for i in range(self.cols):
            for j in range(self.rows):
                w = s.width / self.cols
                h = s.height / self.rows
                v = self.field[i][j].copy()
                v.setMag(w * 0.5)
                x = i * w + w / 2
                y = j * h + h / 2
                strokeWeight(1)
                line(x, y, x + v.x, y + v.y)

    # {.code-wide} A function to return a p5.Vector based on a position
    def lookup(self, position):
        column = constrain(floor(position.x / self.resolution), 0, self.cols - 1)
        row = constrain(floor(position.y / self.resolution), 0, self.rows - 1)
        return self.field[column][row].copy()
