from functools import reduce
from operator import xor

#part 2 in part 1
list_size = 256
def part1(data):
    lst = [i for i in range(0, list_size)]
    current_pos = lst[0]
    skip = 0
    lengths = [ord(i) for i in data]
    lengths.extend([17, 31, 73, 47, 23]) #part2
    print(lengths)
    for j in range(64): #part 2
        for l in lengths:
            last_i = current_pos + l
            rem = last_i - list_size
            r = []
            if rem > 0:
                for i in range(current_pos, list_size):
                    r.append(lst[i])
                for i in range(0, min(rem, current_pos)):
                    r.append(lst[i])
                for i in range(current_pos, list_size):
                    lst[i] = r.pop()
                for i in range(0, rem):
                    lst[i] = r.pop()
            else:
                rem = last_i
                lst[current_pos:last_i] = reversed(lst[current_pos:last_i])
            
            new_pos = rem + skip
            while new_pos >= list_size:
                new_pos -= list_size
            
            current_pos = new_pos
            skip += 1
    
    # Part 2
    dense_hash = []
    for i in range(0, list_size, 16):
        res = reduce(xor, lst[i: i+16])
        dense_hash.append(res)
    
    print(dense_hash)
    hex_str = ''
    for d in dense_hash:
        if len(hex(d)[2:]) != 2:
            hex_str += '0'
        hex_str += hex(d)[2:]
        

    return hex_str, lst[0] * lst[1] #Part1 and part2