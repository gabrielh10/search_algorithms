class Cell():
            # A cell object knows about its location in the grid 
            # it also knows of its size with the variables x,y,w,h.
            def __init__(self, tempX, tempY, tempW, tempH, food, obstacle, explored):
                self.x = tempX
                self.y = tempY
                self.w = tempW
                self.h = tempH
                self.food = food
                self.obstacle = obstacle
                self.explored = 0
                
            def display(self):
                #print(self.obstacle)
                if self.obstacle != 0:                
                    self.obstacle.display()
                elif self.food != 0:
                    self.food.display()   
                elif self.explored != 0 and self.obstacle == 0:
                    stroke(255)
                    fill(255,255,0)
                    rect(self.x,self.y, 20, 20)
                else:    
                    stroke(255)
                    fill(127)
                    rect(self.x,self.y, 20, 20)
                    
            def getNeighbours(self, grid):
                list = []
                if self.w > 0:        #left neighbour
                    list.append(grid[self.w - 1][self.h])
                if self.h > 0:        #up neighbour   
                    list.append(grid[self.w][self.h-1])
                if self.w < 19:       #right neighbour
                    list.append(grid[self.w+1][self.h])
                if self.h < 19:       #down neighbour
                    list.append(grid[self.w][self.h+1])   
                            
                return list
