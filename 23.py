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


def jump(i, val, r, registers):
    if type(r) == str:
        if registers[r] != 0:
            i += val
        else:
            i += 1
    else:
        if r != 0:
            i += val
        else:
            i += 1
    return i


def part1(data):
    registers, steps, length = process_data(data)
    i = 0
    count = 0
    while i < length and i >= 0:
        t = steps[i][0]
        r = steps[i][1]
        try:
            val = registers[steps[i][2]]
        except KeyError:
            val = steps[i][2]
        if t == "set":
            registers[r] = val
        elif t == "sub":
            registers[r] -= val
        elif t == "mul":
            registers[r] *= val
            count += 1
        elif t == "jnz":
            i = jump(i, val, r, registers)
            continue

        i += 1

    return count

def part2(data):
    # Simplified the instructions 
    b = (57 * 100) + 100000
    c = b + 17000
    h = 0
    while 1:
        for j in range(2, b):
            if b % j == 0:
                h += 1
                break
        if b == c:
            break
        b += 17
    
    return h
