def find_empty_tile(initial_state):
    empty_tile = 0  # Index of the empty tile
    row_number = 0  # The row that contains the empty tile
    for row in initial_state:
        row_number += 1
        for tile in row:
            if tile == 0:
                empty_tile = row.index(0)
                return row_number, empty_tile


def swap_row_elements(row, e1, e2):  # Swaps two values in a row
    new_row = row.copy()
    e1_inx = row.index(e1)
    e2_inx = row.index(e2)
    new_row.remove(e2)
    new_row.insert(e2_inx, e1)
    new_row.remove(e1)
    new_row.insert(e1_inx, e2)
    return new_row


def swap_column_elements(r1, r2, e1, e2):
    inx_e1 = r1.index(e1)
    inx_e2 = r2.index(e2)
    row_1 = r1.copy()
    row_2 = r2.copy()
    row_1.pop(inx_e1)
    row_2.pop(inx_e2)
    row_1.insert(inx_e1, e2)
    row_2.insert(inx_e2, e1)
    return row_1, row_2


def swap_right(row, empty_tile, initial_state):  # Swaps the right element with empty tile
    right_element = initial_state[row-1][empty_tile+1]
    new_row = swap_row_elements(initial_state[row-1], 0, right_element)
    return new_row


def swap_left(row, empty_tile, initial_state):
    left_element = initial_state[row-1][empty_tile-1]
    new_row = swap_row_elements(initial_state[row-1], 0, left_element)
    return new_row


def swap_underneath(row, empty_tile, initial_state):
    underneath_element = initial_state[row][empty_tile]
    new_row_1, new_row_2 = swap_column_elements(initial_state[row-1], initial_state[row], 0, underneath_element)
    return new_row_1, new_row_2


def swap_above(row, empty_tile, initial_state):
    above_element = initial_state[row-2][empty_tile]
    new_row_1, new_row_2 = swap_column_elements(initial_state[row-1], initial_state[row-2], 0, above_element)
    return new_row_1, new_row_2