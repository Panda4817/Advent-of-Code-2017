def part1(data):
    stack = []
    nums = [0]
    current_total = 0
    ignore_next = False
    garbage = False
    total_garbage = 0
    for c in data:
        if ignore_next:
            ignore_next = False
            continue
        if c == '{' and garbage != True:
            stack.append(c)
            nums.append(nums[-1] + 1)
        elif c == '<' and garbage == False:
            garbage = True
        elif c == '!':
            ignore_next = True
        elif c == '>' and garbage == True:
            garbage = False
        elif c == '}' and garbage != True:
            stack.pop()
            current_total += nums.pop()
        
        elif garbage:
            total_garbage += 1

    return current_total, total_garbage # part1, part2