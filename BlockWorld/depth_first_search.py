from expand import *
import visualise


def reached_goal(state):
    if state[2][0] == 4 and state[2][1] == 4 and state[3][0] == 4 and state[3][1] == 4:
        return True
    else:
        return False


def depth_first_search(initial_state):
    successors = [initial_state]
    not_goal_states = []
    state_index = 0
    end = 1
    expanded_initial_state = False
    while state_index < end:
        print(successors[state_index])
        if not expanded_initial_state:
            initial_state_successor = find_successors(initial_state)
            successors.append(initial_state_successor[0])
            successors.pop(0)
            end = len(successors)
            expanded_initial_state = True
            continue
        if reached_goal(successors[state_index]):
            print('FOUND GOAL')
            break
        successor = find_successors(successors[state_index])
        for state in successor:
            if state not in successors and state != initial_state and state not in not_goal_states:
                successors.append(state)
                break
        state_index += 1
        end = len(successors)
        if state_index == end:
            not_goal_states.append(successors[state_index-1])
            successors.pop(end-1)
            state_index -= 2
            end = len(successors)

    return successors


state = 'PLEASE ENTER A VALID STATE HERE' \
        'PLEASE MAKE SURE THAT YOUR STATE HAS THE FOLLOWING BLOCKS:' \
        '2 GREEN BLOCKS ( ONE VERITCAL AND THE OTHER HORIZONTAL)' \
        '1 RED BLOCK' \
        '6 BLUE BLOCKS' \
        '2 EMPTY BLOCKS '
visualise.start_simulation(depth_first_search(state))
