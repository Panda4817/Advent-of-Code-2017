hex = {
    'n': [0, 1, -1],
    's': [0, -1, 1],
    'ne': [1, 0, -1],
    'se': [1, -1, 0],
    'sw': [-1, 0, 1],
    'nw': [-1, 1, 0]
}

def part1(data):
    current = [0, 0, 0]
    dirs = data.split(",")
    highest = 0
    for d in dirs:
        current[0] += hex[d][0]
        current[1] += hex[d][1]
        current[2] += hex[d][2]
        
        # Part 2
        m = max(abs(current[0]), abs(current[1]), abs(current[2]))
        if m > highest:
            highest = m
    
    print(current)
    return highest, max(abs(current[0]), abs(current[1]), abs(current[2])) # Part2 and part 1