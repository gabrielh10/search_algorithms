# The "Food" class

class Food():
    #x,y are positions at the grid and factor de size of the grid
    def __init__(self, x, y, factor):
        self.acceleration = PVector(0, 0)
        self.position = PVector(x*factor,y*factor) #real pixel position
        self.factor = factor #size of each grid tile 
        self.grid = PVector(x,y) #position at the grid
        self.r = factor
        self.color = color(0,255,255)

    # Method to update food location
    def update(self, x, y):    
        newPos = PVector(x * self.factor,y * self.factor)
        self.position = newPos
        #c = color (random(255), random(255), random(255))
        #self.color = c
        
    def display(self):
        fill(self.color)
        noStroke()
        strokeWeight(1)
       # with pushMatrix():
        rect(self.position.x, self.position.y, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
