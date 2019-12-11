from Maze import Maze
import requests
import json

def get(path):
    baseURL = "https://api.noopschallenge.com"
    url = "".join([baseURL, path])
    res = requests.get(url)
    return res.json()

def post(path, json):
    baseURL = "https://api.noopschallenge.com"
    url = "".join([baseURL, path])
    res = requests.post(url, json=json)
    return res.json()

def postSolution(solution, postPath):
    return post(postPath, {"directions": solution})

def getSampleMaze(path):
    with open(path) as handle:
        sampleMazeJSON = json.load(handle)
    return sampleMazeJSON

def getRandomMaze(minSize, maxSize):
    basePath = "/mazebot/random"
    args = ""
    if (minSize and maxSize):
        args = f"?minSize={minSize}&maxSize={maxSize}"
    path = "".join([basePath, args])
    return get(path)

def startRace(username):
    path = "/mazebot/race/start"
    startingMazeUrl = post(path, {"login": username})["nextMaze"]
    maze = Maze(get(startingMazeUrl))

    print(maze.mazePath)
    solution = maze.solve()
    print(solution)
    res = postSolution(solution, maze.mazePath)
    nextMaze = res["nextMaze"]

    while nextMaze:
        maze = Maze(get(nextMaze))
        print(maze.mazePath)
        solution = maze.solve()
        print(solution)
        res = postSolution(solution, maze.mazePath)
        print(res)
        nextMaze = res["nextMaze"]

def doSolveRandomMaze(minSize = 60, maxSize =  60):
    maze = Maze(getRandomMaze(minSize,maxSize))
    solution = maze.solve()
    print(solution)
    res = postSolution(solution, maze.mazePath)
    print(res)

def doRaceChallenge(username = "bcowell"):
    startRace(username)

def doSolveSampleMaze():
    path = "sampleMaze.json"
    maze = Maze(getSampleMaze(path))
    solution = maze.solve()
    print(solution)

def main():
    #doSolveRandomMaze()
    #doRaceChallenge()
    doSolveSampleMaze()

if __name__ == "__main__":
    main()