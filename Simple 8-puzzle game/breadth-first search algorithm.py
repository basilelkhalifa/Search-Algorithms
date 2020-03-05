from tiles import *

def find_successor_state(initial_state, expanded_states):
    row, empty_tile = find_empty_tile(initial_state)
    if row == 1:
        if empty_tile == 0:
            expanded_states.append([swap_right(row, empty_tile, initial_state), initial_state[1], initial_state[2]])
            row_1, row_2 = swap_underneath(row, empty_tile, initial_state)
            expanded_states.append([row_1, row_2, initial_state[2]])
        elif empty_tile == 1:
            row_1, row_2 = swap_underneath(row, empty_tile, initial_state)
            expanded_states.append([row_1, row_2, initial_state[2]])
            expanded_states.append([swap_right(row, empty_tile, initial_state), initial_state[1], initial_state[2]])
            expanded_states.append([swap_left(row, empty_tile, initial_state), initial_state[1], initial_state[2]])

        elif empty_tile == 2:
            expanded_states.append([swap_left(row, empty_tile, initial_state), initial_state[1], initial_state[2]])
            row_1, row_2 = swap_underneath(row, empty_tile, initial_state)
            expanded_states.append([row_1, row_2, initial_state[2]])

    elif row == 2:
        if empty_tile == 0:
            expanded_states.append([initial_state[0], swap_right(row, empty_tile, initial_state), initial_state[2]])
            row_1, row_2 = swap_above(row, empty_tile, initial_state)
            expanded_states.append([row_2, row_1, initial_state[2]])
            row_1, row_2 = swap_underneath(row, empty_tile, initial_state)
            expanded_states.append([initial_state[0], row_1, row_2])
        elif empty_tile == 1:
            expanded_states.append("DONE")
        elif empty_tile == 2:
            expanded_states.append([initial_state[0], swap_left(row, empty_tile, initial_state), initial_state[2]])
            row_1, row_2 = swap_above(row, empty_tile, initial_state)
            expanded_states.append([row_2, row_1, initial_state[2]])
            row_1, row_2 = swap_underneath(row, empty_tile, initial_state)
            expanded_states.append([initial_state[0], row_1, row_2])

    elif row == 3:
        if empty_tile == 0:
            expanded_states.append([initial_state[0], initial_state[1], swap_right(row, empty_tile, initial_state)])
            row_1, row_2 = swap_above(row, empty_tile, initial_state)
            expanded_states.append([initial_state[0], row_2, row_1])
        elif empty_tile == 1:
            row_1, row_2 = swap_above(row, empty_tile, initial_state)
            expanded_states.append([initial_state[0], row_2, row_1])
            expanded_states.append([initial_state[0], initial_state[1], swap_right(row, empty_tile, initial_state)])
            expanded_states.append([initial_state[0], initial_state[1], swap_left(row, empty_tile, initial_state)])

        elif empty_tile == 2:
            expanded_states.append([initial_state[0], initial_state[1], swap_left(row, empty_tile, initial_state)])
            row_1, row_2 = swap_above(row, empty_tile, initial_state)
            expanded_states.append([initial_state[0], row_2, row_1])


def expand(initial_state):
    expanded_states = []
    find_successor_state(initial_state, expanded_states)  # takes the state and adds the successors to the given list
    return expanded_states


def graph_search(initial_state):
    path = []
    expansions = [initial_state]
    counter = 0
    while counter < len(expansions):
        expanded = expand(expansions[counter])
        if "DONE" in expanded:
            if expansions[counter] not in path:
                path.append(expansions[counter])
            return path
        expansions.extend(expanded)
        path.append(expansions[(2**counter)-1])
        counter += 1
