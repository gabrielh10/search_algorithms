# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

class Vehicle():

    def __init__(self, x, y, factor):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x*factor, y*factor)
        self.factor = factor
        self.grid = PVector(x,y)
        self.r = 20
        self.maxspeed = 4
        self.maxforce = 0.2

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)
        
    def checkColision(self, obstacles):
        for obstacle in obstacles:
            vector = self.position - obstacle.position
            if(vector.mag() < 10):
                self.velocity = PVector(-1,-1)

    

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, target):

        # A vector pointing from the location to the target
        desired = target - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        fill(255,0,0)
        stroke(200)
        strokeWeight(1)
        circle(self.position.x+10, self.position.y+10, self.r)
         #   with pushMatrix():
          #  translate(self.position.x, self.position.y)
           # rotate(theta)
           # beginShape()
           #vertex(0, -self.r * 2)
           # vertex(-self.r, self.r * 2)
           # vertex(self.r, self.r * 2)
           # endShape(CLOSE)
            
