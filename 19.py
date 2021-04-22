def process_data(data):
    lines = [list(l) for l in data.split("\n")]
    i = 0
    for c in lines[0]:
        if c == '|':
            start = (0, i)
            break
        i += 1
    return lines, start

def get_new_dir(new_dirs, map, r, c, dirs):
    for d in new_dirs:
        try:
            if map[r + dirs[d][0]][c + dirs[d][1]] != ' ':
                current_dir = d
                break
        except IndexError:
            continue
    return current_dir

def part1(data):
    map, start = process_data(data)
    dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]
    current_dir = 0
    r = start[0]
    c = start[1]
    letters = [] # Part 1
    steps = 0 # Part 2
    while 1:
        r += dirs[current_dir][0]
        c += dirs[current_dir][1]
        steps += 1
        if map[r][c] == '|' or map[r][c] == '-':
            continue
        elif ord(map[r][c]) >= ord('A') and ord(map[r][c]) <= ord('Z'):
            letters.append(map[r][c])
            continue
        elif map[r][c] == '+':
            if current_dir in [0, 1]:
                current_dir = get_new_dir([2, 3], map, r, c, dirs)
            else:
                current_dir = get_new_dir([0, 1], map, r, c, dirs)
            continue
        elif map[r][c] == ' ':
            break
    
    return "".join(letters), steps # Part1 and part 2