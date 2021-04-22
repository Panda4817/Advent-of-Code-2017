from collections import deque

def process_data(data):
    registers = {}
    instructions = [l.split() for l in data.split("\n")]
    length = len(instructions)
    for i in range(length):
        for j in range(3):
            if j == 0:
                continue
            try:
                n = int(instructions[i][j])
                instructions[i][j] = n
            except IndexError:
                continue
            except ValueError:
                if instructions[i][j] not in registers:
                    registers[instructions[i][j]] = 0

    return registers, instructions, length

def part1(data):
    registers, steps, length = process_data(data)
    last_sent_freq = 0
    recovered_freq = 0
    i = 0
    while i < length:
        t = steps[i][0]
        r = steps[i][1]
        if len(steps[i]) == 3:
            try:
                val = registers[steps[i][2]]
            except KeyError:
                val = steps[i][2]

        if t == "set":
            registers[r] = val
        elif t == 'add':
            registers[r] += val
        elif t == 'mul':
            registers[r] *= val
        elif t == 'mod':
            registers[r] = registers[r] % val
        elif t == 'snd':
            last_sent_freq = registers[r]
        elif t == 'rcv':
            if registers[r] != 0:
                recovered_freq = last_sent_freq
                break
        elif t == 'jgz':
            if registers[r] > 0:
                i += val
                continue
        
        i += 1

    return recovered_freq

def recover_vars(steps, registers, i):
    t = steps[i][0]
    r = steps[i][1]
    val = None
    if len(steps[i]) == 3:
        try:
            val = registers[steps[i][2]]
        except KeyError:
            val = steps[i][2]
    return t, r, val

def manipulate_values(t, registers, val, r):
    changed = False
    if t == "set":
        registers[r] = val
        changed = True
    elif t == 'add':
        registers[r] += val
        changed = True
    elif t == 'mul':
        registers[r] *= val
        changed = True
    elif t == 'mod':
        registers[r] = registers[r] % val
        changed = True
    
    return registers, changed

def jump(i, val, r, registers):
    if type(r) == str:
        if registers[r] > 0:
            i += val
        else:
            i += 1
    else:
        if r > 0:
            i += val
        else:
            i += 1
    return i


def part2(data):
    registers0, steps0, length0 = process_data(data)
    registers1, steps1, length1 = process_data(data)
    registers1['p'] = 1
    q0 = deque([])
    q1 = deque([])
    
    i = 0
    j = 0

    deadlock0 = False
    deadlock1 = False

    values_sent_by_1 = 0

    while i < length0 or j < length1:
        if i < length0:
            t0, r0, val0 = recover_vars(steps0, registers0, i)
        else:
            t0, r0, val0 = None, None, None
        
        if j < length1:
            t1, r1, val1 = recover_vars(steps1, registers1, j)
        else:
            t1, r1, val1 = None, None, None
        
        registers1, changed1 = manipulate_values(t1, registers1, val1, r1)
        registers0, changed0 = manipulate_values(t0, registers0, val0, r0)
        if changed0:
            i += 1
        if changed1:
            j += 1
        
        if t0 == 'jgz':
            i = jump(i, val0, r0, registers0)
        if t1 == 'jgz':
            j = jump(j, val1, r1, registers1)
        
        if t0 == 'snd':
            q1.append(registers0[r0])
            i += 1
        if t1 == 'snd':
            q0.append(registers1[r1])
            j += 1
            values_sent_by_1 += 1
        
        if t0 == 'rcv' and q0:
            registers0[r0] = q0.popleft()
            i += 1
            deadlock0 = False
        elif t0 == 'rcv':
            deadlock0 = True
        
        if t1 == 'rcv' and q1:
            registers1[r1] = q1.popleft()
            j += 1
            deadlock1 = False
        elif t1 == 'rcv':
            deadlock1 = True
        
        if deadlock1 and deadlock0:
            break

    return values_sent_by_1