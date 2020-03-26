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
    while state_index < 60:
        state = successors[state_index]
        if reached_goal(state):
            print('GOAL FOUND')
            break
        successor_states = find_successors(state)
        for successor_state in successor_states:
            if successor_state in successors:
                successor_states.remove(successor_state)
        successors.extend(successor_states)
        state_index += 1
        end = len(successors)
    print(successors)







