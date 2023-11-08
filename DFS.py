from pyMaze import maze, agent, COLOR
#-----------------------------------------------------------------------------
def DFS(maze):  # takes a maze object of any size
    start = (maze.rows, maze.cols)  # the start cell is the bottom-down cell
    explored_cells = [start]
    frontier = [start]
    dfs_path = {}
    while len(frontier) != 0:
        current_cell = frontier.pop()
        if current_cell == (1, 1):  # if reached goal cell
            break
        for direction in 'ESNW':
            if maze.maze_map[current_cell][direction] == True:
                if direction == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif direction == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif direction == 'S':
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif direction == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])
                if child_cell in explored_cells:
                    continue
                explored_cells.append(child_cell)
                frontier.append(child_cell)
                dfs_path[child_cell] = current_cell
    forward_path = {}
    cell = (1, 1)
    while cell != start:
        forward_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]
    return forward_path
#-----------------------------------------------------------------------------
# main program
row_num = 20
col_num = 30

m = maze(row_num, col_num)
m.CreateMaze()

path = DFS(m)
a = agent(m, footprints=True)
m.tracePath({a:path})  # {agent : the path we want the agent to follow}

m.run()  # show the result