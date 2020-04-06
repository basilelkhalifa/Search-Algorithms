from expand import *
import math
import visualise


def reached_goal(state):
    if state[2][0] == 4 and state[2][1] == 4 and state[3][0] == 4 and state[3][1] == 4:
        return True
    else:
        return False


def a_star_heuristic(state):
    x = ''
    y = ''
    for states in state:
        for value in states:
            if value == 4:
                x = states.index(value)
                y = state.index(states) - 1
                break
    h = round(math.sqrt((x**2 + y**2)), 1)
    return h


def a_star_search(initial_state):
    expanded_states = [(initial_state, 0)]
    visited = []
    while True:
        next_expand = min(expanded_states, key = lambda t: t[1])
        if reached_goal(next_expand[0]):
            print('GOAL FOUND')
            return next_expand[0]
        successors = find_successors(next_expand[0])
        expanded_states.remove(next_expand)
        for successor in successors:
            if successor not in visited:
                expanded_states.append((successor, a_star_heuristic(successor)+1))
                visited.append(successor)


state = 'PLEASE ENTER A VALID STATE HERE' \
        'PLEASE MAKE SURE THAT YOUR STATE HAS THE FOLLOWING BLOCKS:' \
        '2 GREEN BLOCKS ( ONE VERITCAL AND THE OTHER HORIZONTAL)' \
        '1 RED BLOCK' \
        '6 BLUE BLOCKS' \
        '2 EMPTY BLOCKS '
' EXAMPLE STATE [ [1,2,1,1], [1,2,4,4], [2,2,4,4], [1,1,0,0] ]'
visualise.start_simulation(a_star_search(state))