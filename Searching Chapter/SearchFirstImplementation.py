# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    is_explored = []
    possible_paths = [[init[0],init[1],0]]
    path = []
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    for i in range(len(grid)):
        is_explored_inter = []
        for j in range(len(grid[0])):
            if init[0] == i and init[1] == j:
                is_explored_inter.append(1)
            else:
                is_explored_inter.append(0)
            
        is_explored.append(is_explored_inter)
    min_path_index= 0
    min_path_value = 0
    if len(possible_paths) == 0:
        print 'fails'
        return 0
    for idx,possible_path in enumerate(possible_paths):
        if possible_path[2] > min_path_value:
            min_path_index = idx
            min_path_value = possible_path[2]
    
    for action in delta:
                
    return path
