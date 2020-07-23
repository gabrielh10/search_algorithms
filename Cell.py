class Cell():
            # A cell object knows about its location in the grid 
            # it also knows of its size with the variables x,y,w,h.
            def __init__(self, tempX, tempY, tempW, tempH, food, obstacle, explored, path, frontier):
                self.x = tempX
                self.y = tempY
                self.w = tempW
                self.h = tempH
                self.food = food
                self.obstacle = obstacle
                self.explored = 0
                self.path = 0
                self.frontier = 0
                
            def display(self):
                #print(self.obstacle)
                if self.obstacle != 0:                
                    self.obstacle.display()
                elif self.food != 0:
                    self.food.display()   
                elif self.path != 0 and self.obstacle == 0:
                    stroke(255)
                    fill(0,255,0)
                    rect(self.x,self.y, 20, 20)
                elif self.explored != 0 and self.obstacle == 0:
                    stroke(255)
                    fill(255,255,0)
                    rect(self.x,self.y, 20, 20)
                elif self.frontier != 0 and self.obstacle == 0:
                    stroke(255)
                    fill(0,50,200)
                    rect(self.x,self.y, 20, 20)
                else:    
                    stroke(255)
                    fill(127)
                    rect(self.x,self.y, 20, 20)
                    
            def getNeighbours(self, grid):
                list = []
        
                if self.h < 19:       #down neighbour
                    if grid[self.w][self.h+1].obstacle == 0:
                        list.append(grid[self.w][self.h+1])  
                if self.h > 0:        #up neighbour   
                    if grid[self.w][self.h-1].obstacle == 0:
                        list.append(grid[self.w][self.h-1])
                if self.w > 0:        #left neighbour
                    if grid[self.w-1][self.h].obstacle == 0:
                        list.append(grid[self.w - 1][self.h])
                if self.w < 19:       #right neighbour
                    if grid[self.w+1][self.h].obstacle == 0:
                        list.append(grid[self.w+1][self.h])
                       
                return list
                                
            def getNeighboursWithCost(self, grid, root):
                list = []                    
                if self.h < 19:       #down neighbour
                    if grid[self.w][self.h+1].obstacle == 0:
                        cost = grid[self.w][self.h+1].distL1(root.w, root.h)
                        list.append((grid[self.w][self.h+1], cost) )  
                if self.h > 0:        #up neighbour   
                    if grid[self.w][self.h-1].obstacle == 0:
                        cost = grid[self.w][self.h-1].distL1(root.w, root.h)
                        list.append((grid[self.w][self.h-1], cost))
                if self.w > 0:        #left neighbour
                    if grid[self.w-1][self.h].obstacle == 0:
                        cost = grid[self.w - 1][self.h].distL1(root.w, root.h)
                        list.append((grid[self.w - 1][self.h], cost))
                if self.w < 19:       #right neighbour
                    if grid[self.w+1][self.h].obstacle == 0:
                        cost = grid[self.w+1][self.h].distL1(root.w, root.h)
                        list.append((grid[self.w+1][self.h], cost))
                       
                return list
            
            def distL1(self,x2,y2):
                return int(abs(x2-self.h)+abs(y2-self.w))
            
            def __eq__(self, other):         
                if not isinstance(other, Cell):
                    print("not")
                    return 0
                if self.w == other.w and self.h == other.h:
                    print("Self:", self.w, self.h, " Other:",other.w,other.h)
                
                return self.w == other.w and self.h == other.h
            
            def __hash__(self):
                return hash(self.w) + hash(self.h)
