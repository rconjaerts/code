'''
Problem: Robot in a Grid
Description: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
Solved: True
'''

def is_out_grid(grid, location):
    return location[0] >= len(grid) or location[1] >= len(grid[0])

def is_off_limits(grid, location):
    return grid[location[0]][location[1]]

def find_path(grid, curr_location, curr_path, end):
    if is_out_grid(grid, curr_location) or is_off_limits(grid, curr_location):
        return None
    elif curr_location == end:
        curr_path.append(curr_location)
        return curr_path
    else:
        curr_path.append(curr_location)
        return max(find_path(grid, [curr_location[0]+1, curr_location[1]], curr_path, end), find_path(grid, [curr_location[0], curr_location[1]+1], curr_path, end))

# grid consists out of an array in an array where the values can be True, or False. True means the field is OFF LIMITS, False is walkable.
grid = [
    [False, False, False, False, False],
    [False, True, True, False, False],
    [False, False, True, True, False],
    [False, False, False, False, False]
]
print(find_path(grid, [0,0], [], [3, 4]))