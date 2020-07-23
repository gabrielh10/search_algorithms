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
from Queue import PriorityQueue

def bfsTeste(grid):
    visited = set()
    frontier = []    
    frontier = [(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]
    #print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node, path = frontier.pop(0)  
        node.explored = 1
        node.display()        
        visited.add(node)
        for neighbour in node.getNeighbours(grid):
            #print("N:", int(neighbour.w), int(neighbour.h))
            if neighbour.w == int(food.grid.x) and neighbour.h == int(food.grid.y):
                print("sucesso!", neighbour.x, neighbour.y)  
                return path + [neighbour]
            else:     
                if neighbour not in visited:
                    visited.add(neighbour)
                    frontier.append( (neighbour, path+[neighbour]) )
    print("Neightbours:",node.getNeighbours(grid))
    print("LenFront:", len(frontier))
    print("LenVisited:", len(visited))


def dfsTeste(grid):
    visited = set()
    frontier = []    
    #print(vehicle.grid)
    frontier = [(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]
    #print("Food:", int(food.grid.x), int(food.grid.y))
    while(len(frontier) > 0):
        node, path = frontier.pop()  
        node.explored = 1
        visited.add(node)
        for neighbour in node.getNeighbours(grid):
            if neighbour.w == int(food.grid.x) and neighbour.h == int(food.grid.y):
                #print("sucesso!")  
                return path + [neighbour]
            else:     
                if neighbour not in visited:
                    visited.add(neighbour)
                    frontier.append( (neighbour, path+[neighbour]) )
    print("Neightbours:",node.getNeighbours(grid))
    print("LenFront:", len(frontier))
    print("LenVisited:", len(visited))

def distL1(x1,y1,x2,y2):
    return int(abs(x2-x1)+abs(y2-y1))

def shuffle( curNode,gVal,x1, y1, x2, y2):
        
    hVal = 0
    gVal = gVal+1
    if x2 >= 0 and x2 < nCols and y2 >= 0 and y2 < nRows:
        if grid[x2][y2].obstacle!=0:
            return None
        temp_puz = [grid[int(x2)][int(y2)],[hVal,gVal],[grid[int(x2)][int(y2)]]]
        #[(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]               
        return temp_puz
    else:
        return None


def generateChildAStar(curNode,gVal):
    val_list = [[curNode.w, curNode.h - 1], [curNode.w, curNode.h + 1], [curNode.w - 1, curNode.h], [curNode.w + 1, curNode.h]]
    nodes = []
    for i in val_list:
        child = shuffle( curNode,gVal,curNode.w, curNode.h, i[0], i[1])
        if child is not None:
           nodes.append(child)
    return nodes

                     
def aStarSearch(grid):
    visited = {}
    frontier = []    
    hVal = distL1(vehicle.grid.x,vehicle.grid.y,food.grid.x,food.grid.y) 
    gVal = 0 
    frontier = [( grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [hVal,gVal], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] ) ]                        
               #[(grid[int(vehicle.grid.x)][int(vehicle.grid.y)], [grid[int(vehicle.grid.x)][int(vehicle.grid.y)]] )]
    iteration = 0
    frontNodes = 1
    testedNodes = 0
    
    #frontier = PriorityQueue()
    #frontier.put(i)
    #frontier.get()
    print("L1:",distL1(food.grid.x,food.grid.y, food.grid.x,food.grid.y))
    while True:      
        
        cur,fVal,path = frontier.pop(0)
        #print(cur)
        testedNodes += 1
        visited[cur] = fVal[0]+fVal[1]
        cur.explored = 1
        """ If the difference between current and goal node is 0 we have reached the goal node"""
        #print(cur.w,cur.h,food.grid.x,food.grid.y)
        #print("L1(curNode,Food):",distL1(cur.w,cur.h, food.grid.x,food.grid.y))
        if (distL1(cur.w,cur.h, food.grid.x,food.grid.y) == 0):
            return path+[cur]
        for child in generateChildAStar(cur, fVal[1]):
            #heuristic to compute distance between current node and goal
            
            hVal = distL1(child[0].w,child[0].h,food.grid.x,food.grid.y)
            gVal = child[1][1]
            #print(hVal,gVal)
            #print(child[0].w,child[0].h,food.grid.x,food.grid.y,hVal,gVal)                      
            frontNodes += 1
            if child[0] not in visited or (hVal+gVal)<visited[child[0]]:                
                    frontier.append( (child[0], [hVal,gVal], path+[child[0]]) )
                    visited[child[0]] = hVal+gVal
                    
        #if cur not in visited:                
        #  visited.add(cur)
        
    
        """ sort the opne list based on f value """
        #print(frontier)
        
        
        frontier.sort(key=lambda x: x[1][0]+x[1][1], reverse=False)
        # for f in frontier:
        #   print(f[0].w,f[0].h,f[1])
        #print(frontNodes) 
        #print(len(frontier))  
        iteration = iteration + 1
        #if iteration == 100:
        #    break
        
    
                     
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
        obstacle = Obstacle(int(random(nCols)),int(random(nRows)),gridXi,gridYi, sizeGrid)
        listObstacles.append(obstacle)

def obstaclesToGrid(list):
    for i in xrange(nCols):
        for j in xrange(nRows):
            for o in list:
                if o.grid.x == i and o.grid.y == j:
                    grid[i][j] = Cell(gridXi+i*cellW,gridYi+j*cellH,i,j, 0, o, 0, 0)

def clearGrid(grid):
    for i in xrange(nCols):
        for j in xrange(nRows):
            grid[i][j].explored = 0
            grid[i][j].path = 0
            
def setFoodRandomPositium():
    fX = int(random(nCols))
    fY = int(random(nRows))
    while (grid[fX][fY].obstacle!=0):
                       
        fX = int(random(nCols))
        fY = int(random(nRows))
        
    return Food(fX,fY,gridXi,gridYi, sizeGrid)
    
    
nCols = 20;
nRows = 20;
sizeGrid = 20;
cellH = 20;
cellW = 20
result = []
windowH = (nCols+2)*cellW
windowW = (nRows+2)*cellH
gridXi = 20
gridYi = 20
gridXf = 400
gridYf = 400
textH   = 14
foodH   = 12
def setup():
    global vehicle, food, obstacle,listObstacles, counter, textY, textH, windowW, windowH, foodH, nCols, nRows, grid, sizeGrid, result
    size(windowH, windowW)    
    velocity = PVector(gridXi, gridYi)
    #vehicle = Vehicle(int(19), int(19), gridXi, gridYi,sizeGrid)
    vehicle = Vehicle(int(random(nCols)), int(random(nRows)), gridXi, gridYi,sizeGrid)
    vehicle.position.x=gridXf
    vehicle.position.y=gridYf
    

    counter = 0
    listObstacles = []
    generateObstacles(10)
    grid = makeGrid()
    
    
    
    
    
    
    for i in xrange(nCols):
        for j in xrange(nRows):             
            grid[i][j] = Cell(gridXi+i*cellW,gridYi+j*cellH,i,j, 0, 0, 0, 0)
                
    obstaclesToGrid(listObstacles)
    
    #food = Food(int(10), int(10),gridXi,gridYi, sizeGrid)
    #food = Food(int(0), int(0),gridXi,gridYi, sizeGrid)
    #food = Food(int(random(nCols)), int(random(nRows)),gridXi,gridYi, sizeGrid)
    food = setFoodRandomPositium()

    print("InSetup")    
    
    #result = dfsTeste(grid)
    #result = bfsTeste(grid)
    result = aStarSearch(grid)

    for el in result:
         el.path = 1
    
    frameRate(20)

def draw():
    global counter, result,food
    background(255)
    #food.update(10, 10)
    #food.update(0, 0)
    
    target = PVector(food.position.x , food.position.y)
    
    for i in xrange(nCols):
        for j in xrange(nRows):
            # Oscillate and display each object
            if food.grid.x == i and food.grid.y == j:
                #grid[i][j].food = food
                #vector = vehicle.position - target
                if vehicle.grid.x == food.grid.x and vehicle.grid.y == food.grid.y :
                    #food.update(int(random(nCols)), int(random(nRows)))
                    food = setFoodRandomPositium()                
                    #food.update(10, 10)
                    #food.update(0, 0)
                    #vehicle.position.x= gridXf
                    #vehicle.position.y= gridYf
                    #vehicle.grid.y=19
                    #vehicle.grid.x=19
                    #vehicle.position.x= gridXf
                    #vehicle.position.y= gridYf
                    #vehicle.grid.y=int(random(nRows))
                    #vehicle.grid.x=int(random(nCols))
                     
                    clearGrid(grid)
                    
                    #result = dfsTeste(grid)
                    #result = bfsTeste(grid)
                    result = aStarSearch(grid)
                    if result:
                        for el in result:
                            #print(el.x, el.y)
                            el.path = 1
                    else:
                        print("Result veio None")
                        print(result)
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
    
