from blist import blist

def part1(data):
    n = int(data)
    current_pos = 0
    buffer = blist([0])
    value_after = 0
    l = 1
    for i in range(1, 2018):
        current_pos += n
        while current_pos >= l:
            current_pos -= l

        buffer.insert(current_pos + 1, i)

        if i == 2017:
            value_after = buffer[current_pos + 2]
        
        current_pos = current_pos + 1
        l += 1
    print(value_after)
    return buffer, current_pos # Part1

def part2(data):
    buffer, current_pos = part1(data)
    n = int(data)
    l = 2018
    for i in range(2018, 50000000 + 1):
        current_pos += n
        while current_pos >= l:
            current_pos -= l
            
        buffer.insert(current_pos + 1, i)
        
        current_pos = current_pos + 1
        l += 1
    return buffer[1] # part 2