import random

'''
This is an optimized generator for the tile coloring problem.
Because the input file format is not clearly indicated in the project instruction and the original generator does not work
(have bugs in Professor Arora's orininal script), I adapted it using python and now it works on my end. 
This generator does the same function as the one on Github.
It will output landscape,tiles,colorTarget. Landscape is a complex matrix with all colors in each location.
tiles are those with their unique shapes.
colorTarget is state of landscape which we are trying to achieve using the csp algorithm.
'''
# Number 5 stands for the tile blocking area
fullBlock = ((5,5,5,5),(5,5,5,5),(5,5,5,5),(5,5,5,5))
outerBoundary = ((5,5,5,5),(5,0,0,5),(5,0,0,5),(5,5,5,5))
EL1 = ((5,5,5,5),(5,0,0,0),(5,0,0,0),(5,0,0,0))
EL2 = ((5,0,0,0),(5,0,0,0),(5,0,0,0),(5,5,5,5))
EL3 = ((0,0,0,5),(0,0,0,5),(0,0,0,5),(5,5,5,5))
EL4 = ((5,5,5,5),(0,0,0,5),(0,0,0,5),(0,0,0,5))
landscape = []
tiles = []
colorTarget = {}

# Change the height and width will change the given landscape area
height = 16
width = 16

# a function that generates random bushes
def generateRandomBushes(height,width):
    colors = 4

    # generate bushes with value 1/2/3/4
    for i in range(height):
        row = []
        for j in range(width):
            row.append(int((colors)* random.random()+1))
        landscape.append(row)
    
    return landscape


# a function that generates a single tile
def getTile():

    def randomEL():
        if random.random() < 1/4:
            return "EL1"
        elif random.random() < 2/4:
            return "EL2"
        elif random.random() < 3/4:
            return "EL3"
        else:
            return 'EL4'


    if random.random() < 1/3:
        return "fullBlock"
    elif random.random() < 2/3:
        return "outerBoundary"
    else:
        return randomEL()


# return the dictionary colorTarget {1:0,2:0,3:0,4:0}
def calculateTiles(tiles):  
  # generate the target
    counter = 0
    colorTarget = {1:0,2:0,3:0,4:0}
    def getBL(width,counter):
        xDistance = counter % (width/4)
        yDistance = counter // (width/4)
        return int(xDistance*4),int(yDistance*4)
    for tile in tiles:
        # x and y are bottlmleft point of the given tile.
        x,y = getBL(width,counter)

        if tile == "outerBoundary":
            colorTarget[landscape[x+1][y+1]] += 1
            colorTarget[landscape[x+1][y+2]] += 1
            colorTarget[landscape[x+2][y+1]] += 1
            colorTarget[landscape[x+2][y+2]] += 1

        if tile == "EL1":
            colorTarget[landscape[x+1][y]] += 1
            colorTarget[landscape[x+1][y+1]] += 1
            colorTarget[landscape[x+1][y+2]] += 1
            colorTarget[landscape[x+2][y]] += 1
            colorTarget[landscape[x+2][y+1]] += 1
            colorTarget[landscape[x+2][y+2]] += 1
            colorTarget[landscape[x+3][y]] += 1
            colorTarget[landscape[x+3][y+1]] += 1
            colorTarget[landscape[x+3][y+2]] += 1
    
        elif tile == "EL2":
            colorTarget[landscape[x+1][y+1]] += 1
            colorTarget[landscape[x+1][y+2]] += 1
            colorTarget[landscape[x+1][y+3]] += 1
            colorTarget[landscape[x+2][y+1]] += 1
            colorTarget[landscape[x+2][y+2]] += 1
            colorTarget[landscape[x+2][y+3]] += 1
            colorTarget[landscape[x+3][y+1]] += 1
            colorTarget[landscape[x+3][y+2]] += 1
            colorTarget[landscape[x+3][y+3]] += 1

        elif tile == "EL3":
            colorTarget[landscape[x][y]] += 1
            colorTarget[landscape[x][y+1]] += 1
            colorTarget[landscape[x][y+2]] += 1
            colorTarget[landscape[x+1][y]] += 1
            colorTarget[landscape[x+1][y+1]] += 1
            colorTarget[landscape[x+1][y+2]] += 1
            colorTarget[landscape[x+2][y]] += 1
            colorTarget[landscape[x+2][y+1]] += 1
            colorTarget[landscape[x+2][y+2]] += 1

        elif tile == "EL4":
            colorTarget[landscape[x][y+1]] += 1
            colorTarget[landscape[x][y+2]] += 1
            colorTarget[landscape[x][y+3]] += 1
            colorTarget[landscape[x+1][y+1]] += 1
            colorTarget[landscape[x+1][y+2]] += 1
            colorTarget[landscape[x+1][y+3]] += 1
            colorTarget[landscape[x+2][y+1]] += 1
            colorTarget[landscape[x+2][y+2]] += 1
            colorTarget[landscape[x+2][y+3]] += 1

        counter += 1

    return colorTarget


def problemGenerator():

    # generates the tiles
    numTiles = height * width // 16
    landscape = generateRandomBushes(height,width)
    # generate all tiles
    for i in range(numTiles):
        tiles.append(getTile())

    colorTarget = calculateTiles(tiles)

    return landscape,tiles,colorTarget

#problemGenerator()
#print(landscape,tiles,colorTarget)