import copy
# The algorithms work by swapping the values of the blocks with the empty areas to move the block
# For example, when the "red" function is called with the direction set to 'down', it swaps the top 2 values (4, 4)
# with the two zeros below it


# Controls the movement of the red block
def red(direction, position, state):
    row, col = position  # Position is a tuple containing the row and column of the block
    state_copy = copy.deepcopy(state)
    if direction == 'down':
        state_copy[row][col] = state[row+2][col]
        state_copy[row + 2][col] = state[row][col]
        state_copy[row][col+1] = state[row+2][col+1]
        state_copy[row+2][col+1] = state[row][col+1]
        return state_copy
    elif direction == 'up':
        state_copy[row-1][col] = state[row + 1][col]
        state_copy[row + 1][col] = state[row-1][col]
        state_copy[row-1][col + 1] = state[row + 1][col + 1]
        state_copy[row + 1][col + 1] = state[row - 1][col + 1]
        return state_copy
    elif direction == 'left':
        state_copy[row][col+1] = state[row][col-1]
        state_copy[row][col - 1] = state[row][col+1]
        state_copy[row+1][col + 1] = state[row+1][col - 1]
        state_copy[row+1][col - 1] = state[row+1][col + 1]
        return state_copy
    elif direction == 'right':
        state_copy[row][col + 2] = state[row][col]
        state_copy[row][col] = state[row][col + 2]
        state_copy[row+1][col + 2] = state[row+1][col]
        state_copy[row + 1][col] = state[row+1][col + 2]
        return state_copy


# Controls the movement of a blue block
def blue(direction, position, state):
    row, col = position
    state_copy = copy.deepcopy(state)
    if direction == 'down':
        state_copy[row][col] = state[row+1][col]
        state_copy[row+1][col] = state[row][col]
        return state_copy
    elif direction == 'up':
        state_copy[row][col] = state[row - 1][col]
        state_copy[row - 1][col] = state[row][col]
        return state_copy
    elif direction == 'right':
        state_copy[row][col] = state[row][col+1]
        state_copy[row][col+1] = state[row][col]
        return state_copy
    elif direction == 'left':
        state_copy[row][col] = state[row][col - 1]
        state_copy[row][col - 1] = state[row][col]
        return state_copy


# Controls the movement of the horizontal green block
def horizontal_green(direction, position, state):
    row, col = position
    state_copy = copy.deepcopy(state)
    if direction == 'up':
        state_copy[row][col] = state[row-1][col]
        state_copy[row-1][col] = state[row][col]
        state_copy[row][col+1] = state[row-1][col+1]
        state_copy[row-1][col+1] = state[row][col+1]
        return state_copy
    elif direction == 'down':
        state_copy[row][col] = state[row + 1][col]
        state_copy[row + 1][col] = state[row][col]
        state_copy[row][col + 1] = state[row + 1][col + 1]
        state_copy[row + 1][col + 1] = state[row][col + 1]
        return state_copy
    elif direction == 'right':
        state_copy[row][col] = state[row][col+2]
        state_copy[row][col+2] = state[row][col]
        return state_copy
    elif direction == 'left':
        state_copy[row][col + 1] = state[row][col - 1]
        state_copy[row][col - 1] = state[row][col + 1]
        return state_copy


# Controls the movement of teh vertical green block
def vertical_green(direction, position, state):
    row, col = position
    state_copy = copy.deepcopy(state)
    if direction == 'up':
        state_copy[row+1][col] = state[row-1][col]
        state_copy[row-1][col] = state[row+1][col]
        return state_copy
    elif direction == 'down':
        state_copy[row][col] = state[row+2][col]
        state_copy[row+2][col] = state[row][col]
        return state_copy
    elif direction == 'right':
        state_copy[row][col] = state[row][col+1]
        state_copy[row][col + 1] = state[row][col]
        state_copy[row+1][col] = state[row+1][col+1]
        state_copy[row + 1][col + 1] = state[row+1][col]
        return state_copy
    elif direction == 'left':
        state_copy[row][col] = state[row][col - 1]
        state_copy[row][col - 1] = state[row][col]
        state_copy[row + 1][col] = state[row + 1][col - 1]
        state_copy[row + 1][col - 1] = state[row + 1][col]
        return state_copy


# Move block given a color
def move(color, direction, position, state, axis=None):
    if color == 'red':
        return red(direction, position, state)
    elif color == 'blue':
        return blue(direction, position, state)
    elif color == 'green' and axis == 'horizontal':
        return horizontal_green(direction, position, state)
    elif color == 'green' and axis == 'vertical':
        return vertical_green(direction, position, state)

