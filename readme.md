
indexing is the same as matrix indexing, top left cell being the 1st row and 1st column
the goal is the green cell (which is cell (1,1))
the maze is perfect: there is only one path from **any cell** to (1, 2) 


# 💡 Abstract: 
A maze-solving algorithm is an automated method for solving a maze. In fact, Maze-solving algorithms are closely related to graph theory; if one pulled and stretched out the paths in the maze in the proper way, the result could be made to resemble a tree! <br>
Here, a famous algorithm called "recursive backtracker" is used to generate random mazes each time the program is being run. 
It's worthy of mention that mazes containing no loops are known as "simply connected", or "perfect" mazes, and are equivalent to a tree in graph theory and this is a critical piece of info to keep in mind while designing sush algorithms.
This repo is a collection of maze solving algorithms I've learned through my "Algorithmic Graph Theory" course at university (SBU)

# How Does The Code Work?
There are several files in this repo:
- `pyMaze.py`
- `DFS.py`
used stack to implement. 
- `BFS.py`
Breadth-First searched is garanteed to give the **shortest path** while being an **un-informed** of **blind** search.
Of course, a queue is used to perform bfs.
The `BFS_path` is a dictionary like this: child_cell:currecnt_cell
- `A_star.py`
an informed algorithm
# Resources


	
