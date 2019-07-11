import requests
import json

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # distance between the current and start node
        self.h = 0  # estimated distance from current to end node
        self.f = 0  # total cost of the node

    def __eq__(self, compare):
        return self.position == compare.position

    def __str__(self):
        return "pos=%s, g=%s, h=%s, f=%s" % (self.position, self.g, self.h, self.f)

    # Returns list of four nearest neighbour Nodes
    def generateChildren(self, maze):

        neighbourNodes = []
        maxX = len(maze[0]) - 1
        maxY = len(maze) - 1

        x = self.position[0]
        y = self.position[1]
        adj = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]
        
        # Remove any out-of-bounds and walls
        for a in adj:
            x = a[0]
            y = a[1]
            if x >= 0 and y >= 0 and x <= maxX and y <= maxY:
                # Maze from api is a 2D array
                # Meaning maze[0] is an array of x's at y=0
                if maze[y][x] != 'X':
                    neighbourNodes.append(Node(self, a))
        return neighbourNodes

def aStar(maze, start, goal):

    openSet = [start]  # list of nodes to evaluate
    closedSet = []  # list of nodes already evaltuated

    # Returns the sum of the absolute difference of the x and y coords
    def distanceDiff(start, end):
        h = [x - y for (x, y) in zip(start.position, end.position)]
        return sum([abs(x) for x in h])

    # Converts a list of coordinates to their respective directions
    # IE. [[0,1], [0,2], [1,2], ...] returns "SE..."
    def convertCoordsToDirections(coords):

        def findDirection(curr, next):
            difference = [x - y for (x, y) in zip(next, curr)]
            x = difference[0]
            y = difference[1]
            if x != 0:
                if x > 0:
                    return 'E'
                elif x < 0:
                    return 'W'
            elif y != 0:
                if y > 0:
                    return 'S'
                elif y < 0:
                    return 'N'

        dirs = ''
        for i, coord in enumerate(coords):
            if (i+1 >= len(coords)): return dirs
            nextCoord = coords[i+1]
            direction = findDirection(coord, nextCoord)
            dirs = ''.join([dirs,direction])
        #return dirs

    while len(openSet):
        # Get the node with the least f value
        openSet = sorted(openSet, key=lambda node: node.f)
        currentNode = openSet.pop(0)
        closedSet.append(currentNode)

        # Found the goal
        if currentNode == goal:
            print('Found goal')
            # backtrack to get coords traversed
            coords = []
            curr = currentNode
            while curr is not None:
                coords.append(curr.position)
                curr = curr.parent
            # coords are reversed from backtracking
            coords.reverse()
            solution = convertCoordsToDirections(coords)
            print(solution)
            break

        # Generate children (four nearest neighbours)
        children = currentNode.generateChildren(maze)

        for child in children:
            if child in closedSet:
                continue

            # create g,h,f values
            child.g = currentNode.g + distanceDiff(child, currentNode) # dist between child and current
            child.h = distanceDiff(child, goal) # distance from end
            child.f = child.g + child.h

            # if child in openSet:
            # if child.g is GT the openSet node's g
            for openNode in openSet:
                if child == openNode and child.g > openNode.g:
                    continue

            # add child to openSet
            openSet.append(child)

def getRandomMaze():
    url = 'https://api.noopschallenge.com/mazebot/random'
    res = requests.get(url)
    return res.json()['map']

def main():

    maze = [["X", "X", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", "X", "X", "X", " ", "X", "X", " "],
            ["X", "X", " ", "X", " ", "X", " ", "X", " ", " "],
            [" ", " ", " ", " ", " ", "X", " ", "X", " ", "X"],
            [" ", "X", "X", " ", "X", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", "X", " ", "X", " ", " "],
            [" ", "X", " ", "X", " ", " ", " ", "X", " ", "X"],
            [" ", "X", " ", "X", " ", "X", "X", "X", " ", " "],
            [" ", "X", "X", "X", " ", " ", "A", " ", "X", " "],
            [" ", " ", " ", "B", "X", " ", " ", "X", " ", " "]]
    startingPosition = Node(None, [6, 8])
    endingPosition = Node(None, [3, 9])
    aStar(maze, startingPosition, endingPosition)
    #maze = getRandomMaze()
    #print(maze)


if __name__ == "__main__":
    main()