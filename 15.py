from collections import deque

a = 289
b = 629

a_factor = 16807
b_factor = 48271
divide_by = 2147483647

rounds = 5000000 #40000000 - part1
lowest = 15

def next_val(letter, prev):
    if letter == 'a':
        factor = a_factor
    else:
        factor = b_factor
    
    n = prev * factor
    return n % divide_by

def part1(data):
    prev_a = a
    a_bin = ''
    prev_b = b
    b_bin = ''
    matching = 0
    for i in range(rounds):
        next_a = next_val('a', prev_a)
        a_bin = bin(next_a)[2:].zfill(32)
        prev_a = next_a
        
        next_b = next_val('b', prev_b)
        b_bin = bin(next_b)[2:].zfill(32)
        prev_b = next_b
        
        if a_bin[-1:lowest:-1] == b_bin[-1:lowest:-1]:
            matching += 1
    
    return matching

def part2(data):
    a_multiple = 4
    b_multiple = 8
    prev_a = a
    a_values = deque([])
    prev_b = b
    b_values = deque([])
    pairs = 0
    matching = 0
    while pairs <= rounds:
        next_a = next_val('a', prev_a)
        prev_a = next_a
        if next_a % a_multiple == 0:
            a_bin = bin(next_a)[2:].zfill(32)
            a_values.append(a_bin)
        
        next_b = next_val('b', prev_b)
        prev_b = next_b
        if next_b % b_multiple == 0:
            b_bin = bin(next_b)[2:].zfill(32)
            b_values.append(b_bin)
        
        if a_values and b_values:
            a_bin = a_values.popleft()
            b_bin = b_values.popleft()
            pairs += 1
            if a_bin[-1:lowest:-1] == b_bin[-1:lowest:-1]:
                matching += 1

    return matching