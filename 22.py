
def process_data(data):
    grid = [[0 if i == '.' else 2 for i in l]for l in data.split("\n")]
    start_r = len(grid) // 2
    start_c = len(grid[0]) // 2
    return grid, start_r, start_c, 'n'


def change_direction(current, new):
    n, s, e, w = 'n', 's', 'e', 'w'
    if current == n:
        r = e
        l = w
    elif current == s:
        r = w
        l = e
    elif current == e:
        l = n
        r = s
    elif current == w:
        r = n
        l = s

    if new == 'r':
        return r
    elif new == 'l':
        return l


def move_forward(facing, r, c, grid):
    n, s, e, w = 'n', 's', 'e', 'w'
    f = {
        n: [-1, 0],
        s: [1, 0],
        e: [0, 1],
        w: [0, -1]
    }

    new_r = r + f[facing][0]
    new_c = c + f[facing][1]
    if new_r == -1:
        new_row = [0 for i in range(len(grid[0]))]
        grid.insert(0, new_row)
        new_r = 0
    elif new_r == len(grid):
        new_row = [0 for i in range(len(grid[-1]))]
        grid.append(new_row)
        new_r = len(grid) - 1

    if new_c == -1:
        for r in range(len(grid)):
            grid[r].insert(0, 0)
        new_c = 0
    elif new_c == len(grid[new_r]):
        for r in range(len(grid)):
            grid[r].append(0)
        new_c = len(grid[new_r]) - 1

    return new_r, new_c, grid


def burst_activity_part1(grid, r, c, facing, num):
    if grid[r][c] == 2:
        facing = change_direction(facing, 'r')
        grid[r][c] = 0
    else:
        facing = change_direction(facing, 'l')
        grid[r][c] = 2
        num += 1

    r, c, grid = move_forward(facing, r, c, grid)
    return grid, r, c, facing, num


def burst_activity_part2(grid, r, c, facing, num):
    if grid[r][c] == 0:
        facing = change_direction(facing, 'l')
        grid[r][c] = 1
    elif grid[r][c] == 1:
        grid[r][c] = 2
        num += 1
    elif grid[r][c] == 2:
        facing = change_direction(facing, 'r')
        grid[r][c] = 3
    elif grid[r][c] == 3:
        facing = change_direction(facing, 'r')
        facing = change_direction(facing, 'r')
        grid[r][c] = 0

    r, c, grid = move_forward(facing, r, c, grid)
    return grid, r, c, facing, num


def print_grid(grid, r, c):
    print(r, c)
    print("=====")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) == (r, c):
                print("[" + str(grid[i][j]) + "]", end="")
            elif (i, j + 1) == (r, c):
                print(grid[i][j], end="")
            else:
                print(grid[i][j], end=" ")
        print()
    print()


def part1(data):
    grid, r, c, facing = process_data(data)
    bursts = 10000
    caused_infection = 0
    for i in range(bursts):
        # print_grid(grid, r, c)
        grid, r, c, facing, caused_infection = burst_activity_part1(
            grid, r, c, facing, caused_infection)
    return caused_infection


def part2(data):
    grid, r, c, facing = process_data(data)
    bursts = 10000000
    caused_infection = 0
    for i in range(bursts):
        # print_grid(grid, r, c)
        grid, r, c, facing, caused_infection = burst_activity_part2(
            grid, r, c, facing, caused_infection)
    return caused_infection
