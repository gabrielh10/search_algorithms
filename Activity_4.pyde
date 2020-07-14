# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario
# Modified by Gabriel Henrique

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food
from Obstacle import Obstacle
from Cell import Cell

#Working, but need some fix at the algorithm visited is equals to frontier (it's shouldn't)
def bfs():
    visited = []
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    visited.append(grid[0][0])
    frontier.append(grid[0][0])
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node = frontier.pop(0)        
        if node.w == int(food.grid.x) and node.h == int(food.grid.y):
            print("sucesso!")  
            return visited
        for neighbour in node.getNeighbours(grid):
           # print(len(frontier))
            #print('Neighbour:', node.w, node.h)
            if neighbour not in visited:
                frontier.append(neighbour)
                visited.append(neighbour)
                
def bfsTeste():
    visited = set()
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    #visited.append(grid[0][0])
    frontier.append(grid[0][0])
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node = frontier.pop(0)  
        visited.add(node)
        if node.w == int(food.grid.x) and node.h == int(food.grid.y):
            print("sucesso!")  
            return visited
        for neighbour in node.getNeighbours(grid):
           # print(len(frontier))
            print('Neighbour:', node.w, node.h)
            if neighbour not in visited:
                frontier.append(neighbour)

def dfs():            
    visited = []
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    visited.append(grid[0][0])
    frontier.append(grid[0][0])
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node = frontier.pop()        
        if node.w == int(food.grid.x) and node.h == int(food.grid.y):
            print("sucesso!")  
            return visited
        for neighbour in node.getNeighbours(grid):
           # print(len(frontier))
            #print('Neighbour:', node.w, node.h)
            if neighbour not in visited:
                frontier.append(neighbour)
                visited.append(neighbour)

def dfsTeste():
    visited = set()
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    #visited.append(grid[0][0])
    frontier.append(grid[0][0])
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node = frontier.pop()  
        visited.add(node)
        if node.w == int(food.grid.x) and node.h == int(food.grid.y):
            print("sucesso!")  
            return visited
        for neighbour in node.getNeighbours(grid):
           # print(len(frontier))
            print('Neighbour:', node.w, node.h)
            if neighbour not in visited:
                frontier.append(neighbour)
                     
def makeGrid():
            global nCols, nRows
            grid = []
            for i in xrange(nCols):
                # Create an empty list for each row
                grid.append([])
                for j in xrange(nRows):
                    # Pad each column in each row with a 0
                    grid[i].append(0)
            return grid

#Add random position obstacles to the listObstacles list
def generateObstacles(quantidade):
    for x in range(quantidade):
        obstacle = Obstacle(int(random(nCols)),int(random(nRows)), sizeGrid)
        listObstacles.append(obstacle)

def obstaclesToGrid(list):
    for i in xrange(nCols):
        for j in xrange(nRows):
            for o in list:
                if o.grid.x == i and o.grid.y == j:
                    grid[i][j] = Cell(i*20,j*20,i,j, 0, o, 0)

nCols = 20;
nRows = 20;
sizeGrid = 20;

def setup():
    global vehicle, food, obstacle,listObstacles, counter, textY, textH, foodH, nCols, nRows, grid, sizeGrid
    size(400, 400)
    textH = height
    textH = 14
    foodH = 12
    velocity = PVector(0, 0)
    vehicle = Vehicle(int(0), int(0), sizeGrid)
    food = Food(int(random(nCols)), int(random(nRows)), sizeGrid)

    counter = 0
    listObstacles = []
    generateObstacles(10)
    
    grid = makeGrid()
    
    for i in xrange(nCols):
        for j in xrange(nRows):
            # Initialize each object
            #print(food.position.x,i)
           # if food.grid.x == i and food.grid.y == j:
            #    grid[i][j] = Cell(i*20,j*20,20,20, food, 0)       
          #  else:
                
            grid[i][j] = Cell(i*20,j*20,i,j, 0, 0, 0)
                
    obstaclesToGrid(listObstacles)
    visited = []
    visited = dfs()
    for el in visited:
        el.explored = 1
        print("Visitados:", el.w, el.h)  
def draw():
    global counter
    background(255)
    target = PVector(food.position.x , food.position.y)
    
    for i in xrange(nCols):
        for j in xrange(nRows):
            # Oscillate and display each object
            if food.grid.x == i and food.grid.y == j:
                #grid[i][j].food = food
                vector = vehicle.position - target
                if vector.mag() < 5:
                    food.update(int(random(20)), int(random(20)))
                    #grid[i][j].food = food
                    counter+=1                    
                
            grid[i][j].display()
    
    #display and update the vehicle position
    #vehicle.arrive(target)
    #vehicle.update()
    vehicle.display()
    
    #display the obstacles at the list
#    for x in listObstacles:
#        x.display()
        
    #vehicle.checkColision(listObstacles)
    
    food.display()
    
    #Display de amount of food collected
    fill(0)
    textSize(textH)
    textAlign(CENTER)
    text('Quantidade de comida coletada: '+str(counter),width/2,height-4)


        #print('Comidas Coletadas:',counter)
    
