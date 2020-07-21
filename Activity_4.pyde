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
import time

#Working, but need some fix at the algorithm visited is equals to frontier (it's shouldn't)
def bfs(grid):
    visited = []
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    visited.append(grid[0][0])
    frontier.append(grid[0][0])
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node = frontier.pop(0) 
        if node not in visited:
            print("node:",node.w, node.h)
            node.path = 1
            visited.append(node)  
        if node.w == int(food.grid.x) and node.h == int(food.grid.y):
            #print("sucesso!")  
            return visited
        for neighbour in node.getNeighbours(grid):
           # print(len(frontier))
            #print('Neighbour:', node.w, node.h)
            if (neighbour not in visited) or (neighbour not in frontier) or neighbour.explored == 1:
                #print("frontier:",neighbour.w, neighbour.h)
                neighbour.explored = 1
                frontier.append(neighbour)
                #visited.append(neighbour)
            #else:
                #print("n:",neighbour)
    return None       
def bfsTeste(grid):
    visited = set()
    frontier = []    
    
    print(vehicle.grid.x, vehicle.grid.y)
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    #visited.append(grid[0][0])
    frontier = [(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node, path = frontier.pop(0)  
        node.explored = 1
        visited.add(node)
        for neighbour in node.getNeighbours(grid):
            if neighbour.w == int(food.grid.x) and neighbour.h == int(food.grid.y):
                print("sucesso!")  
                return path + [neighbour]
            else:     
                if neighbour not in visited:
                    visited.add(neighbour)
                    frontier.append( (neighbour, path+[neighbour]) )

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

def dfsTeste(grid):
    visited = set()
    frontier = []    
  #  visited.append(grid[vehicle.grid.x][vehicle.grid.y])
  #  frontier.append(grid[vehicle.grid.x][vehicle.grid.y])
    #visited.append(grid[0][0])
    frontier = [(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]
    print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node, path = frontier.pop()  
        node.explored = 1
        visited.add(node)
        for neighbour in node.getNeighbours(grid):
            if neighbour.w == int(food.grid.x) and neighbour.h == int(food.grid.y):
                print("sucesso!")  
                return path + [neighbour]
            else:     
                if neighbour not in visited:
                    visited.add(neighbour)
                    frontier.append( (neighbour, path+[neighbour]) )
                     
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
                    grid[i][j] = Cell(i*20,j*20,i,j, 0, o, 0, 0)

def clearGrid(grid):
    for i in xrange(nCols):
        for j in xrange(nRows):
            grid[i][j].explored = 0
            grid[i][j].path = 0

nCols = 20;
nRows = 20;
sizeGrid = 20;
result = []

def setup():
    global vehicle, food, obstacle,listObstacles, counter, textY, textH, foodH, nCols, nRows, grid, sizeGrid, result
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
                
            grid[i][j] = Cell(i*20,j*20,i,j, 0, 0, 0, 0)
                
    obstaclesToGrid(listObstacles)
    
    result = bfsTeste(grid)
    for el in result:
         el.path = 1
    #    print("Result:", el.w, el.h)

 #   visited = []
 #   visited = bfs()
 #   for el in visited:
 #        el.explored = 1
 #       print("Visitados:", el.w, el.h)  
def draw():
    global counter, result
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
                    print("NewFood:", food.grid.x, food.grid.y)
                    clearGrid(grid)
                    result = bfsTeste(grid)
                    
                    for el in result:
                        print(el.x, el.y)
                        el.path = 1
                    #grid[i][j].food = food
                    counter+=1                    
                
                
            grid[i][j].display()
    
    #result = bfsTeste(grid)
    #for el in result:
    #    el.path = 1
    #    print("Result:", el.w, el.h)

    vehicle.update()
    vehicle.display()
    
    vehicle.move(result)

    food.display()
    #bfs()
    #time.sleep(0.1)
    #Display de amount of food collected
    fill(0)
    textSize(textH)
    textAlign(CENTER)
    text('Quantidade de comida coletada: '+str(counter),width/2,height-4)


        #print('Comidas Coletadas:',counter)
    
