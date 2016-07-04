# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------
def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value  = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    initial_state = list(init)
    #value[initial_state[0]][initial_state[1]] = 0
    while change:
        change = False
        print 'next iteration \n'
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y]  = 0
                        policy[x][y] = '*'
                        change = True
                        print 'reached'

                elif grid[x][y] == 0:
                    change_detect = False
                    min_value     = value[x][y]
                    min_action    = 0
                    min_initial_state_temp = 0
                    for a in range(len(action)):
                        initial_state_temp = (initial_state[2] + action[a])%(len(action))
                        #print initial_state[2]
                        x2 = x + forward[initial_state_temp][0]
                        y2 = y + forward[initial_state_temp][1]
                        
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost[a]
                            #print 'possible value for inner loop v2 ',v2
                            if v2 < min_value:
                                change_detect = True
                                #print 'possible value for inner loop'
                                change    = True
                                min_value = v2
                                min_action= a
                                min_initial_state_temp = initial_state_temp
                    if change_detect == True:
                        value [x][y] = min_value
                        policy[x][y] = action_name[min_action]
                        initial_state[2] = min_initial_state_temp
                        print 'x ', x, ' y ', y, ' value ', v2,' action ' ,action_name[min_action]
        for out in policy:
            print out,'\n'
    return policy
    
def optimum_policy2D(grid,init,goal,cost):

    return policy2D
    
output = optimum_policy(grid,goal,cost)
for out in output:
    print out,'\n'
