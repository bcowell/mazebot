
# Solution
A* Search implemented in python.

## Profiling
This [noops challenge](https://noopschallenge.com) is to a race to solve a series of mazes in a row. 

I've heard how variations of A* are the preffered way to do pathfinding in video games. And thought it would be fun to try my hand at coding it.

It also means that this program will likely go through many iterations as I learn to profile and optimize python.

In the future I wil include a folder for profile logs including a git hash to link profiles to a specific commit.

## Sample output
```
Found goal
WWNNNNNNNNNNNNEEEEEEESSSSSSEENNNNNNEEEENNNEESSSSSSSSEENNEEEENNNNNNNEEEEEEEEESSSSEEEESEEEEEEEEESSSSSWWWSSESSSWSSSSSSEENNNNNEESEEEEEEEEEESEEESSSSEESSSSSWWWSWWWWWWWWWWWWWWWSSEESSSSSESSSSWWNNNWNNNWWSSSWWWWNNNWWSWWWSSWWWWSSWWWWWWWWWWWWWWNNNWWSSWWSSSWWSSSWWSSSWWSSSWWNNNNNEENNNEENNNNNNNNNNNNNNNEESSSEEEENNNNNEESSSSSEENNNNNEENEESSSEEENEENNNEEEEEESSSSWWWSSW
{'result': 'success', 'message': 'You solved it in 0.551 seconds with 349 steps. The shortest possible solution is 323 steps.', 'shortestSolutionLength': 323, 'yourSolutionLength': 349, 'elapsed': 551}
```

# 👋 Mazebot

![Mazebot animation](https://user-images.githubusercontent.com/212941/59631813-9ad09f80-90fd-11e9-8556-810c48531558.gif)

# 🤖 API

Each maze in Mazebot's collection has a map that is a an array of rows.

Each row is an array of single-length strings representing the contents of each location in the maze.

The possible values are:

- `" "` empty - a passable square
- `"X"` - wall - not passable
- `"A"` - starting position - this is where you start in the maze
- `"B"` - goal - this is where you need to navigate to to escape the maze

The rows are in order from north to south, and the entries in each column are in order from west to east.

In these mazes, you may travel in any of the four cardinal directions ("N", "E", "S", "W").

## ✳️ How to play

Mazebot offers two ways to play: random mode, and the great maze race.

See the [API documentation](./API.md) for more information.

## 🎲 Random mode

Mazebot will give you a random selection from its maze collection and see how fast you can solve it.

You can optionally limit the sizes of maze you would like with the `minSize` and `maxSize` parameters.

### Get a random maze

`GET /mazebot/random`

### Get a maze that is at least 20 squares wide.

`GET /mazebot/random?minSize=20`

### Get a maze that is between 30 and 60 squares wide.

`GET /mazebot/random?minSize=30&maxSize=60`

## 🏎️ Race mode

In race mode, mazebot will give you a series of mazes and challenge you to solve them all. At the end, if you are successful, Mazebot will award you a certificate that you can use to prove your maze mettle.

###  Get information about the race

`GET /mazebot/race`

###  Start the race

`POST /mazebot/race { "login": "yourgithubnamehere" }`

More about Mazebot here: https://noopschallenge.com/challenges/mazebot