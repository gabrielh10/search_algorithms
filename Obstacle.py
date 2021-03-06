# The "Food" class

class Obstacle():

    
        
    def __init__(self, x, y, xi,yi,factor):
        self.r = 20
        self.color = color(0,0,0)
        self.xi = xi
        self.yi = yi
        self.position = PVector(x*factor+xi,y*factor+yi) #real pixel position
        self.factor = factor #size of each grid tile 
        self.grid = PVector(x,y) #position at the grid

    # Method to update food location
    def update(self, x, y):    
        newPos = PVector(x * self.factor+self.xi,y * self.factor+self.yi)
        self.position = newPos

    def display(self):
        fill(self.color)
        noStroke()
        strokeWeight(1)
        rect(self.position.x, self.position.y, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
