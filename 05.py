# Part 2 in part 1
def part1(data):
  offsets = [int(num) for num in data.split("\n")]
  i = 0
  steps = 0
  length = len(offsets)
  while i < length:
    o = offsets[i]
    if o >= 3:
      offsets[i] -= 1
    else:
      offsets[i] += 1
    i += o
    steps += 1
  
  return steps
  
    
