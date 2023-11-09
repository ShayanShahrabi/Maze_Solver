from pyMaze import maze, agent, COLOR, textLabel
#-----------------------------------------------------------------------------
def BFS(maze): # takes a maze object of any size
    start_cell = (m.rows, m.cols)
    frontier_list = [start_cell]
    explored_list = [start_cell]
    bfs_path = {}  # stores key:value like child_cell:parent_cell so it stores the reverse of desired path
    while len(frontier_list) > 0:
        current_cell = frontier_list.pop()
        if current_cell == (1, 1):  # if reached the goal
            break
        for direction in 'ESNW':
            if m.maze_map[current_cell][direction] == True:
                if direction == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif direction == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif direction == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])
                else:  # direction == 'W'
                    child_cell = (current_cell[0] + 1, current_cell[1])
                if child_cell in explored_list:
                    continue
                frontier_list.append(child_cell)
                explored_list.append(child_cell)
                bfs_path[child_cell] = current_cell
    forward_path = {}  # stores the correct order of the path from start to finish
    cell = (1,1)
    while cell != start_cell:
        forward_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return forward_path
#-----------------------------------------------------------------------------
# main program
row_num = 10
col_num = 10

m = maze(row_num, col_num)
m.CreateMaze()
path = BFS(m)

a = agent(m, footprints=True, filled=True)
m.tracePath({a:path})
t_label = textLabel(m, 'Length of The Shortest Path', len(path) + 1)

m.run()  # run the simulation