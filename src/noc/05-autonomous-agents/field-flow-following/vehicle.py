from p5 import *
s = get_instance()

class Vehicle:
    def __init__(self, x, y, ms, mf):
        self.position = createVector(x, y)
        self.acceleration = createVector(0, 0)
        self.velocity = createVector(0, 0)
        self.r = 4
        self.maxspeed = ms
        self.maxforce = mf

    def run(self):
        self.update()
        self.borders()
        self.show()

    # Implementing Reynolds' flow field following algorithm
    # http://www.red3d.com/cwr/steer/FlowFollow.html
    def follow(self, flow):
        # What is the vector at that spot in the flow field?
        desired = flow.lookup(self.position)
        # Scale it up by maxspeed
        desired.mult(self.maxspeed)
        # Steering is desired minus velocity
        steer = Vector.sub(desired, self.velocity)
        steer.limit(self.maxforce) # Limit to maximum steering force
        self.applyForce(steer)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset acceleration to 0 each cycle
        self.acceleration.mult(0)

    # Wraparound
    def borders(self):
        if self.position.x < -self.r: self.position.x = s.width + self.r
        if self.position.y < -self.r: self.position.y = s.height + self.r
        if self.position.x > s.width + self.r: self.position.x = -self.r
        if self.position.y > s.height + self.r: self.position.y = -self.r

    def show(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()
        fill(127)
        stroke(0)
        strokeWeight(2)
        with push():
            translate(self.position.x, self.position.y)
            rotate(theta)
            with closedShape():
                vertex(self.r * 2, 0)
                vertex(-self.r * 2, -self.r)
                vertex(-self.r * 2, self.r)
