from pyMaze import maze
#-----------------------------------------------------------------------------
def BFS(maze): # takes a maze object of any size
    start_cell = (m.rows, m.cols)
    frontier_list = []
    explored_list = []
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
#-----------------------------------------------------------------------------
# main program
row_num = 20
col_num = 30

m = maze(row_num, col_num)
m.CreateMaze()

m.run()  # run the simulation