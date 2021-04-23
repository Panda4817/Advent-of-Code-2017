import numpy as np


def convert_num_grid(string):
    string = string.replace(".", "0")
    string = string.replace("#", "1")
    grid = [[int(i) for i in r] for r in string.split("/")]
    np_grid = np.array(grid)
    return np_grid


def process_data(data):
    rules = {}
    lines = data.split("\n")
    for l in lines:
        patterns = l.split(" => ")

        rules[patterns[0]] = {
            'rule': convert_num_grid(patterns[0]),
            'result': convert_num_grid(patterns[1])
        }
    return rules


def break_grid(current_grid, current_size):
    if current_size % 2 == 0:
        cols = current_size // 2
        n = 2
    elif current_size % 3 == 0:
        cols = current_size // 3
        n = 3

    sub_grids = (current_grid.reshape(current_size // n, n, -1,
                                      n).swapaxes(1, 2).reshape(-1, n, n))
    return sub_grids, cols


def is_equal(sub_grid, rule_grid):
    if np.array_equal(sub_grid, rule_grid):
        return True

    if np.array_equal(np.fliplr(sub_grid), rule_grid):
        return True

    if np.array_equal(np.flipud(sub_grid), rule_grid):
        return True

    for r in range(3):
        sub_grid = np.rot90(sub_grid)
        if np.array_equal(sub_grid, rule_grid):
            return True

        if np.array_equal(np.fliplr(sub_grid), rule_grid):
            return True

        if np.array_equal(np.flipud(sub_grid), rule_grid):
            return True

    return False


def part1(data):
    rules = process_data(data)
    current_grid = convert_num_grid('.#./..#/###')
    current_size = 3
    iterations = 5  # Part 2 - 18 iterations
    for i in range(iterations):
        sub_grids, cols_number = break_grid(current_grid, current_size)
        connect = []
        j = 0
        row = []
        for s in sub_grids:
            for v in rules.values():
                if is_equal(s, v['rule']):
                    row.append(v['result'])
                    j += 1
                    break
            if j == cols_number:
                connect.append(row)
                row = []
                j = 0
        current_grid = np.block(connect)
        current_size = len(current_grid)

    return np.count_nonzero(current_grid)
