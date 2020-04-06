from expand import *
import visualise


def reached_goal(state):
    if state[2][0] == 4 and state[2][1] == 4 and state[3][0] == 4 and state[3][1] == 4:
        return True
    else:
        return False


def breadth_first_search_algorithm(initial_state):
    successors = [initial_state]
    state_index = 0
    end = 1
    while state_index < end:
        state = successors[state_index]
        if reached_goal(state):
            print('GOAL FOUND')
            return state
        successor_states = find_successors(state)
        for successor_state in successor_states:
            if successor_state in successors:
                successor_states.remove(successor_state)
        successors.extend(successor_states)
        state_index += 1
        end = len(successors)


state = 'PLEASE ENTER A VALID STATE HERE' \
        'PLEASE MAKE SURE THAT YOUR STATE HAS THE FOLLOWING BLOCKS:' \
        '2 GREEN BLOCKS ( ONE VERITCAL AND THE OTHER HORIZONTAL)' \
        '1 RED BLOCK' \
        '6 BLUE BLOCKS' \
        '2 EMPTY BLOCKS '
' EXAMPLE STATE [ [1,2,1,1], [1,2,4,4], [2,2,4,4], [1,1,0,0] ]'

visualise.start_simulation(breadth_first_search_algorithm(state))
