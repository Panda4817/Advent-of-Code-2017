def part1(data):
    vars = {}
    lst = [l.split() for l in data.split("\n")]
    for l in lst:
        if l[0] not in vars:
            vars[l[0]] = 0
        if l[4] not in vars:
            vars[l[4]] = 0
        l[2] = int(l[2])
        l[-1] = int(l[-1])
    
    def inc(var, num):
        vars[var] += num
    
    def dec(var, num):
        vars[var] -= num
    
    def check_condition(var, condition, num):
        if condition == '>':
            return vars[var] > num
        if condition == '<':
            return vars[var] < num
        if condition == '>=':
            return vars[var] >= num
        if condition == '<=':
            return vars[var] <= num
        if condition == '==':
            return vars[var] == num
        if condition == '!=':
            return vars[var] != num
    
    current_largest = 0 #part 2
    
    for l in lst:
        if check_condition(l[4], l[5], l[6]):
            if l[1] == 'inc':
                inc(l[0], l[2])
            else:
                dec(l[0], l[2])
            
            # part 2
            temp_max = max(vars.values())
            if temp_max > current_largest:
                current_largest = temp_max
    
    return current_largest, max(vars.values()) # part2, part1