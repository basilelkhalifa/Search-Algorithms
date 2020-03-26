import move_block
import copy


class Block:
    def __init__(self, color, position, direction=None):
        self.color = color
        self.position = position
        self.block_direction = direction


def find_empty_space(state):  # Returns a list containing positions of the two zeros in tuples
    zeros = []
    for rows in range(len(state)):
        for columns in range(len(state[rows])):
            if state[rows][columns] == 0:
                zeros.append((rows, columns))
    return zeros


def define_blocks(state, list_blocks):  # Converts values of blocks to objects of blocks
    state_copy = copy.deepcopy(state)
    for rows in range(len(state_copy)):
        for columns in range(len(state_copy[rows])):
            value = state_copy[rows][columns]
            try:
                under_value = state_copy[rows+2][columns]
            except IndexError:
                under_value = 'No value under it'
            if value == 1:
                list_blocks.append(Block('blue', (rows, columns)))
            elif value == 2 and state_copy[rows + 1][columns] == 2 and under_value != 2:
                list_blocks.append(Block('green', (rows, columns), direction='vertical'))
                state_copy[rows + 1][columns] = 'ALREADY DEFINED AS VERTICAL'
            elif value == 2 and state_copy[rows][columns + 1] == 2:
                list_blocks.append(Block('green', (rows, columns), direction='horizontal'))
                state_copy[rows][columns + 1] = 'ALREADY DEFINED AS HORIZONTAL'  # Prevents the algorithm from adding a
                # none existing block
            elif value == 4:
                if not any(block.color == 'red' for block in list_blocks):  # Prevents the algorithm from adding an
                    # existing red block
                    list_blocks.append(Block('red', (rows, columns)))


def zeros_together(zeros_positions):
    if zeros_positions[0][0] == zeros_positions[1][0] and zeros_positions[1][1] - zeros_positions[0][1] == 1:
        return 'horizontally together'
    elif zeros_positions[1][0] - zeros_positions[0][0] == 1 and zeros_positions[0][1] == zeros_positions[1][1]:
        return 'vertically together'
    else:
        return False


def separate_zero_expand(state, zero_position, blocks):
    states = []
    zero_row, zero_column = zero_position
    beside_zero = {'up': None, 'down': None, 'left': None, 'right': None}
    if zero_row != 0:  # Position Above Zero
        beside_zero['down'] = (zero_row - 1, zero_column)
    if zero_row != 3:  # Position Below Zero
        beside_zero['up'] = (zero_row + 1, zero_column)
    if zero_column != 0:  # Position Left to Zero
        beside_zero['right'] = (zero_row, zero_column - 1)
    if zero_column != 3:  # Position Right to Zeros
        beside_zero['left'] = (zero_row, zero_column + 1)
    for direction, position in beside_zero.items():
        for block in blocks:
            if block.color == 'blue' and position == block.position:
                new_state = move_block.move(block.color, direction, block.position, state, axis=block.block_direction)
                states.append(new_state)
            if block.color == 'green' and direction == 'down' and position == (block.position[0]+1, block.position[1])\
                    and block.block_direction == 'vertical':
                new_state = move_block.move(block.color, direction, block.position, state, axis=block.block_direction)
                states.append(new_state)
            if block.color == 'green' and direction == 'right' and position == (block.position[0], block.position[1]+1)\
                    and block.block_direction == 'horizontal':
                new_state = move_block.move(block.color, direction, block.position, state, axis=block.block_direction)
                states.append(new_state)
            if block.color == 'green' and direction == 'up' and position == block.position and \
                    block.block_direction == 'vertical':
                new_state = move_block.move(block.color, direction, block.position, state, axis='vertical')
                states.append(new_state)
            if block.color == 'green' and direction == 'left' and position == block.position and \
                    block.block_direction == 'horizontal':
                new_state = move_block.move(block.color, direction, block.position, state, axis='horizontal')
                states.append(new_state)
    return states


def horizontal_zeros_expand(state, zeros_positions, blocks):
    states = []
    zero_row, zero_column = zeros_positions[0]
    beside_zeros = {'up': None, 'down': None, 'left': None, 'right': None}
    if zero_row != 0:
        beside_zeros['down'] = (zero_row - 1, zero_column)
    if zero_row != 3:
        beside_zeros['up'] = (zero_row + 1, zero_column)
    if zero_column != 0:
        beside_zeros['right'] = (zero_row, zero_column - 1)
    if zero_column != 3:
        beside_zeros['left'] = (zero_row, zero_column + 2)
    for direction, position in beside_zeros.items():
        for block in blocks:
            if block.color == 'red' and direction == 'down' and position == (block.position[0]+1, block.position[1]):
                new_state = move_block.move('red', direction, block.position, state)
                states.append(new_state)
            if block.color == 'red' and direction == 'up' and position == block.position:
                new_state = move_block.move('red', direction, block.position, state)
                states.append(new_state)
            if block.color == 'green' and block.block_direction == 'horizontal' and position == block.position:
                new_state = move_block.move('green', direction, block.position, state, axis='horizontal')
                states.append(new_state)
    states.extend(separate_zero_expand(state, zeros_positions[0], blocks))
    states.extend(separate_zero_expand(state, zeros_positions[1], blocks))
    return states


def vertical_zeros_expand(state, zeros_positions, blocks):
    states = []
    zero_row, zero_column = zeros_positions[0]
    beside_zeros = {'up': None, 'down': None, 'left': None, 'right': None}
    if zero_row != 0:  # Position Above Zero
        beside_zeros['down'] = (zero_row - 1, zero_column)
    if zero_row != 3:  # Position Below Zero
        beside_zeros['up'] = (zero_row + 1, zero_column)
    if zero_column != 0:  # Position Left to Zero
        beside_zeros['right'] = (zero_row, zero_column - 1)
    if zero_column != 3:  # Position Right to Zeros
        beside_zeros['left'] = (zero_row, zero_column + 1)
    for direction, position in beside_zeros.items():
        for block in blocks:
            if block.color == 'green' and block.block_direction == 'vertical' and position == block.position:
                new_state = move_block.move(block.color, direction, position, state, axis='vertical')
                states.append(new_state)
            if block.color == 'red' and direction == 'left' and position == block.position:
                new_state = move_block.move('red', direction, position, state)
                states.append(new_state)
            if block.color == 'red' and direction == 'right' and position == (block.position[0], block.position[1]+1):
                new_state = move_block.move('red', direction, block.position, state)
                states.append(new_state)
    states.extend(separate_zero_expand(state, zeros_positions[0], blocks))
    states.extend(separate_zero_expand(state, zeros_positions[1], blocks))
    return states


def expand_state(state, zeros_positions, blocks):
    if not zeros_together(zeros_positions):
        states = []
        states.extend(separate_zero_expand(state, zeros_positions[0], blocks))
        states.extend(separate_zero_expand(state, zeros_positions[1], blocks))
        return states
    elif zeros_together(zeros_positions) == 'horizontally together':
        return horizontal_zeros_expand(state, zeros_positions, blocks)
    elif zeros_together(zeros_positions) == 'vertically together':
        return vertical_zeros_expand(state, zeros_positions, blocks)


def find_successors(state):
    expanded_states = []
    zeros = find_empty_space(state)
    blocks = []
    define_blocks(state, blocks)
    expanded_states.extend(expand_state(state, zeros, blocks))
    return expanded_states
