class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # distance between the current and start node
        self.h = 0  # estimated distance from current to end node
        self.f = 0  # total cost of the node

    def __eq__(self, compare):
        return self.position == compare.position

    def __str__(self):
        return f"pos={self.position}, g={self.g}, h={self.h}, f={self.f}"

    # Returns list of four nearest neighbour Nodes
    def generateChildren(self, maze, maxX, maxY):
        neighbourNodes = []

        x = self.position[0]
        y = self.position[1]
        adj = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]
        
        # Remove any out-of-bounds and walls
        for a in adj:
            x = a[0]
            y = a[1]
            if x >= 0 and y >= 0 and x < maxX and y < maxY:
                # Maze from api is a 2D array
                # Meaning maze[0] is an array of x's at y=0
                if maze[y][x] != 'X':
                    neighbourNodes.append(Node(self, a))
        return neighbourNodes
