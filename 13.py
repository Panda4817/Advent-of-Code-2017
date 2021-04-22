def process_data(data):
    lst = data.split("\n")
    layers = {}
    for l in lst:
        l_r = [int(i) for i in l.split(": ")]
        layers[l_r[0]] = {"range": l_r[1], "multiple": (l_r[1] - 1)*2}
    
    m = max(layers.keys())
    for i in range(m):
        if i not in layers:
            layers[i] = {"range": 0}
    return layers, m

def part1(data):
    layers, max_layer = process_data(data)
    severity = 0
    offset = 0
    for l in range(max_layer + 1):
        if layers[l]["range"] == 0:
            offset += 1
            continue
        elif offset % layers[l]["multiple"] == 0:
            severity += (l * layers[l]["range"])
        offset += 1
    
    return severity

def part2(data):
    layers, max_layer = process_data(data)
    delay = 0
    while True:
        delay += 1
        offset = 0
        for l in range(max_layer + 1):
            if layers[l]["range"] == 0:
                offset += 1
                continue
            elif (delay + offset) % layers[l]["multiple"] == 0:
                break
            offset += 1
        else:
            break
    
    return delay