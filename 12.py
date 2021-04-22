part1_id = 0

def process_data(data):
    lst = data.split("\n")
    links = {}
    for l in lst:
        key_val = l.split(" <-> ")
        links[int(key_val[0])] = [int(i) for i in key_val[1].split(", ")]
    return links

def part1(data):
    links = process_data(data)
    visited = [part1_id]
    stack = [i for i in links[part1_id]]
    while stack:
        n = stack.pop(0)
        visited.append(n)
        for i in links[n]:
            if i not in visited and i not in stack:
                stack.append(i)
    return len(visited)

def part2(data):
    links = process_data(data)
    groups = 0
    part_of_group = []
    for k in links.keys():
        if k in part_of_group:
            continue
        visited = [k]
        stack = [i for i in links[k]]
        while stack:
            n = stack.pop(0)
            visited.append(n)
            for i in links[n]:
                if i not in visited and i not in stack:
                    stack.append(i)
        part_of_group.extend(visited)
        groups += 1
    return groups