import problemGenerator as generate
import sys
import time

'''
This file implements the CSP algorithm for the tile problem.
Tile problem is a CSP assignment problem. 
'''
fOut = open('output.txt','w')
sys.stdout = fOut
colorOfState = {}
landscape,tiles,colorTarget = generate.problemGenerator()
# fullBlock,outerBoundary,EL1,EL2,EL3,EL4 = generate.fullBlock,generate.outerBoundary,generate.EL1, generate.EL2,generate.EL3,generate.EL4

# This method returns the number of each shape of tiles that a given state have
def getAnswer(tiles):
    # Get the number of each shape of blocks
    numFull,numOuter,numEL = 0,0,0

    for tile in tiles:
        if tile == "fullBlock":
            numFull += 1
        elif tile == "outerBoundary":
            numOuter += 1
        elif tile == "EL1" or tile == "EL2" or tile == "EL3" or tile == "EL4":
            numEL += 1
    return numFull,numOuter,numEL

targetFull, targetOuter, targetEL = getAnswer(tiles) # The initial given condition of the tiles

def heuristics():
    # Pick the block that will achieve the goal easier

    oB,E4,E3,E2,E1 = stack.pop(),stack.pop(),stack.pop(),stack.pop(),stack.pop()
    def colorDiff(colorOfState):
        return colorTarget[1] - colorOfState[1] + colorTarget[2] - colorOfState[2] + colorTarget[3] - colorOfState[3] + colorTarget[4] - colorOfState[4]
    
    # push the state with larger colorDiff first
    priority = [[oB,colorDiff(generate.calculateTiles(oB))],[E1,colorDiff(generate.calculateTiles(E1))],[E2,colorDiff(generate.calculateTiles(E2))],[E3,colorDiff(generate.calculateTiles(E3))],[E4,colorDiff(generate.calculateTiles(E4))]]
    sorted(priority, key = lambda state: state[1],reverse=True)

    for state in priority:
        stack.append(state[0])

    return

# To check if the given state meets the target requirement
def checkMap(colorOfState,colorTarget):
    if colorTarget.get(1) == colorOfState.get(1) and colorTarget.get(2) == colorOfState.get(2) and colorTarget.get(3) == colorOfState.get(3) and colorTarget.get(4) == colorOfState.get(4):
        return True
    return False

# check if the composition of a state is valid
def checkValid(numEL,numFull,numOuter):
    if numEL <= targetEL and numFull <= targetFull and numOuter <= targetOuter:
        return True
    else:
        return False

# Implementing a DFS algorithm with improved features: ordering and filtering
stack = [["Nil" for i in range(len(tiles))]]
map = {}

def DFS():
    # Possible Value: fullBlock outerBoundary EL1 EL2 EL3 EL4
    # use hashmap to check if the given state is visited before
    while stack:
        currentState = stack.pop()

        # If this state is not explored.
        check = tuple(currentState)
        if check in map and map[check] == 2:
            continue
        if check not in map:
            map[check] = 1
            stack.append(currentState)
        elif map[check] == 1:  # if all childs of this state have been explored.
            map[check] = 2

        # Backtracking Increment Goal Test: Check Constraints as you go.
        numFull,numOuter,numEL = getAnswer(currentState)
        if not checkValid(numEL,numFull,numOuter):
            continue

        # print(currentState)
        # print currentState at this moment will reveal all DFS path   
        colorOfState = generate.calculateTiles(currentState)
        if currentState[-1] != "Nil": # if this state have all tiles assigned, check it to see if it is the target
            if checkMap(colorOfState,colorTarget):
                print(currentState)
                print("Calculation Completed")
                print(tiles)
                return currentState        

        else: # if states are not assigned, assign all possible states and add those to the stack
            for i in range(len(tiles)):
                if currentState[i] == "Nil":
                    temp = currentState

                    def addition(adding): # add a given state to the stack.
                        temp[i] = adding
                        add = temp[:]
                        stack.append(add)

                    addition("fullBlock")
                    addition("EL1")
                    addition("EL2")
                    addition("EL3")
                    addition("EL4")
                    addition("outerBoundary")

                    heuristics()
                    break
    return 

print(len(landscape))

start_time = time.time()
DFS()
print("--- %s seconds ---" % (time.time() - start_time))

