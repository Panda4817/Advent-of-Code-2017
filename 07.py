from collections import deque, Counter

def part1(data):
  lst = data.split("\n")
  disks = {}
  for l in lst:
    parts = l.split()
    disks[parts[0]] = {'holding': [], 'weight': int(parts[1][1:-1])}
    if len(parts) == 2:
      continue
    

    disks[parts[0]]['holding'].extend([x if x[-1] != ',' else x[0:-1] for x in parts[3:]])
  
  for k,v in disks.items():
    if v['holding'] == []:
      continue

    bottom = k
    for ke, ve in disks.items():
      if ve['holding'] == [] or ke == k:
        continue
      
      if k in ve['holding']:
        break
    else:
      break
  
  return bottom, disks


class Node():
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
    self.children = []

def part2(data):
  top, disks = part1(data)
  top_node = Node(top, disks[top]['weight'])

  q = deque([(top, top_node)])
  while q:
    name, node = q.popleft()
    for c in disks[name]['holding']:
      new_node = Node(c, disks[c]['weight'])
      node.children.append(new_node)
      q.append((c, new_node))
  
  def recurse(node):
    overall = node.weight
    if node.children == []:
      return overall
    
    for c in node.children:
      overall += recurse(c)
    
    return overall
  
  def all_match(overall_weights):
    if overall_weights == {}:
      return None, 0

    val = [i for i, n in Counter(overall_weights.values()).items() if n == 1]
    
    if val:
      for k, v in overall_weights.items():
        if v == val[0]:
          return k, v
    else:
      return True, 0
    

    
  
  overall_weights = {}
  levels = {}
  values = []
  n = 1
  q = deque([top_node])
  while q:
    node = q.popleft()
    for c in node.children:
      overall_weights[c.name] = (recurse(c))

    ans, val = all_match(overall_weights)
    if val != 0:
      values.append(val)
    for c in node.children:
      if ans == True or ans == None:
        q.append(c)
        continue
      elif c.name == ans:
        q.append(c)
        break
    
    levels[n] = overall_weights
    overall_weights = {}
    n += 1
  

  unbalanced_prog = ''
  diff = 0
  for k, v in levels.items():
    if k == 1:
      for ke, ve in v.items():
        if ve not in values:
          diff = ve - values[0]
          break
    if k == len(values):
      for ke, ve in v.items():
        if ve in values:
          unbalanced_prog = ke
          break
  
  return disks[unbalanced_prog]['weight'] + diff
    


  
    
    

  
  


  