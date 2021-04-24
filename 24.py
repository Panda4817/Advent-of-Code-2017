from copy import deepcopy

def process_data(data):
    components = set([tuple([int(p) for p in l.split("/")])  for l in data.split("\n")])
    zero_ports = []
    for c in components:
        if 0 in c:
            zero_ports.append(c)
    return components, zero_ports

max_strength = 0
max_length = 0
class Node(object):
    def __init__(self, port1, port2, not_used, strength, length):
        global max_strength, max_length
        self.port1 = port1
        self.port2 = port2
        self.strength = strength + port1 + port2
        self.length = length + 1
        self.not_used = not_used
        self.children = []
        if self.length > max_length:
            max_strength = self.strength
            max_length = self.length
        elif self.length == max_length  and self.strength > max_strength:
            max_strength = self.strength
            max_length = self.length
        self.add_children()
    
    def add_children(self):
        for c in self.not_used:
            if self.port2 in c:
                if c[0] == self.port2:
                    p1, p2 = c[0], c[1]
                else:
                    p1, p2 = c[1], c[0]
                components = deepcopy(self.not_used)
                components.remove(c)
                node = Node(
                    p1,
                    p2,
                    components,
                    self.strength,
                    self.length
                )
                self.children.append(node)

def part1(data):
    components, zero_ports = process_data(data)
    for z in zero_ports:
        components.remove(z)
        tree = Node(0, max(z), components, 0, 0)
    return max_strength, max_length # Part1, part2