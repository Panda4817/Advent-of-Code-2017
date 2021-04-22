import math

def part1(data):
  num = int(data)
  n = math.floor(math.sqrt(num)) + 1
  sq = n*n
  steps_from_side = sq - num
  adjust = 0
  while steps_from_side > n:
    steps_from_side = steps_from_side - n
    adjust += 1
  middle = math.floor(n / 2)
  across = abs(middle - steps_from_side)
  up = middle
  return abs(across + up) - adjust

def part2(data):
  num = int(data)
  n = math.floor(math.sqrt(num)) + 2
  grid = [[0]*n for _ in range(n)]
  m = math.floor(n / 2)
  row = m
  col = m
  diameter = 1
  grid[row][col] = 1
  
  def update_grid(r, c):
    s = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        else:
          s += grid[r + i][c + j] 
    return s

  def move_right(r, c):
    return r, c + 1
  
  def move_up(r, c):
    return r - 1, c
  
  def move_left(r, c):
    return r, c - 1

  def move_down(r, c):
    return r + 1, c
  
  while True:
    row, col = move_right(row, col)
    diameter += 2

    grid[row][col] = update_grid(row,col)
    if grid[row][col] > num:
      return grid[row][col]
  
    for i in range(diameter - 2):
      row, col = move_up(row, col)
      grid[row][col]  = update_grid(row,col)
      if grid[row][col] > num:
        return grid[row][col]
    
    for i in range(diameter - 1):
      row, col = move_left(row, col)
      grid[row][col]  = update_grid(row,col)
      if grid[row][col] > num:
        return grid[row][col]
    
    for i in range(diameter - 1):
      row, col = move_down(row, col)
      grid[row][col]  = update_grid(row,col)
      if grid[row][col] > num:
        return grid[row][col]
    
    for i in range(diameter - 1):
      row, col = move_right(row, col)
      grid[row][col]  = update_grid(row,col)
      if grid[row][col] > num:
        return grid[row][col]


  # diameter = 1
  # Repeat below:
  # Move right by 1
  # Incremet diameter by 2
  # Move up by diameter- 2
  # Move left by diameter - 1
  # Move down diameter -1
  # Move right by diameter -1


  



        


  