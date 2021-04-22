from functools import reduce
from operator import xor
from collections import deque

list_size=256
bit_size=128

def knot_hash(input):
    lst = [i for i in range(0, list_size)]
    current_pos = lst[0]
    skip = 0
    lengths = [ord(i) for i in input]
    lengths.extend([17, 31, 73, 47, 23])
    for j in range(64):
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
    
    dense_hash = []
    for i in range(0, list_size, 16):
        res = reduce(xor, lst[i: i+16])
        dense_hash.append(res)
    
    
    hex_str = ''
    for d in dense_hash:
        if len(hex(d)[2:]) != 2:
            hex_str += '0'
        hex_str += hex(d)[2:]
    
    b = bin(int(hex_str, 16))[2:].zfill(bit_size)
    return b

def part1(data):
    num_used = 0
    for i in range(bit_size):
        b = knot_hash(data + str(i))
        num_used += b.count("1")
    return num_used

def get_adj_cells(row, col):
    res = []
    if row != 0:
        res.append((row - 1, col))
    if row != 127:
        res.append((row + 1, col))
    if col != 0:
        res.append((row, col - 1))
    if col != 127:
        res.append((row, col + 1))
    return res

def part2(data):
    grid = []
    for i in range(bit_size):
        b = knot_hash(data + str(i))
        grid.append(list(b))
    regions = 0
    visited = set()
    for r in range(bit_size):
        for c in range(bit_size):
            if (r, c) in visited or grid[r][c] != "1":
                continue
            regions += 1
            stack = deque([(r, c)])
            while stack:
                row, col = stack.popleft()
                visited.add((row, col))
                res = get_adj_cells(row, col)
                for (rr, cc) in res:
                    if (rr, cc) not in visited and grid[rr][cc] == "1":
                        stack.append((rr, cc))
    return regions