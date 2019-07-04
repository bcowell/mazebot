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
                if maze[x][y] != 'X':
                    neighbourNodes.append(Node(self, a))
        return neighbourNodes


def getRandomMaze():
    url = 'https://api.noopschallenge.com/mazebot/random'
    res = requests.get(url)
    return res.json()['map']


def aStar(maze, start, goal):

    openSet = [start]  # list of nodes to evaluate
    closedSet = []  # list of nodes already evaltuated

    # Returns the sum of the absolute difference of the x and y coords
    def diff(start, end):
        h = [x - y for (x, y) in zip(start.position, end.position)]
        return sum([abs(x) for x in h])

    while len(openSet):
        # Get the node with the least f value
        openSet = sorted(openSet, key=lambda node: node.f)
        currentNode = openSet.pop(0)

        # Found the goal
        if currentNode == goal:
            print('Found goal')
            # backtrack to get solution
            solution = []
            curr = currentNode
            while curr is not None:
                solution.append(curr.position)
                curr = curr.parent
            print(solution)
            break

        # Generate children (four nearest neighbours)
        children = currentNode.generateChildren(maze)
        
        for child in children:
            if child in closedSet:
                continue

            # create g,h,f values
            child.g = currentNode.g + diff(child, currentNode) # dist between child and current
            child.h = diff(child, goal) # distance from end
            child.f = child.g + child.h

            if child in openSet:
                # if child.g is GT the openSet node's g
                continue
            # add child to openSet
            openSet.append(child)
        
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