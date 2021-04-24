a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
write = 'write'
move = 'move'
state = 'state'
states = {
    a: {0: {write: 1, move: 1, state: b}, 1: {write: 0, move: 1, state: f}},
    b: {0: {write: 0, move: -1, state: b}, 1:{write: 1, move: -1, state: c}},
    c: {0: {write: 1, move: -1, state: d}, 1:{write: 0, move: 1, state: c}},
    d: {0: {write: 1, move: -1, state: e}, 1:{write: 1, move: 1, state: a}},
    e: {0: {write: 1, move: -1, state: f}, 1:{write: 0, move: -1, state: d}},
    f: {0: {write: 1, move: 1, state: a}, 1:{write: 0, move: -1, state: e}},
}

def move_cursor(new_cursor, machine):
    if new_cursor < 0:
        machine.insert(0, 0)
        new_cursor = 0
    elif new_cursor == len(machine):
        machine.append(0)
    return new_cursor, machine

def part1(data):
    max_steps = 12964419
    machine = [0]
    cursor = 0
    current_state = a
    steps = 0

    while steps != max_steps:
        if machine[cursor] == 0:
            machine[cursor] = states[current_state][0][write]
            cursor += states[current_state][0][move]
            current_state = states[current_state][0][state]
        elif machine[cursor] == 1:
            machine[cursor] = states[current_state][1][write]
            cursor += states[current_state][1][move]
            current_state = states[current_state][1][state]
        cursor, machine = move_cursor(cursor, machine)
        steps += 1
    
    return machine.count(1)


