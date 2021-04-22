# part2 in part 1
def part1(data):
  bank = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
  # bank = [0, 2, 7, 0]

  def get_max(bank):
      m = max(bank)
      for i in range(len(bank)):
          if bank[i] == m:
              return (i, m)

  states = {}
  cycles = 0

  while tuple(bank) not in states:
      states[tuple(bank)] = True
      index, num = get_max(bank)
      bank[index] = 0
      index += 1
      while num > 0:
          if index == len(bank):
              index = 0
          bank[index] += 1
          num -= 1
          index += 1
      cycles += 1
  
  # return cycles - part 1

  aim = tuple(bank)
  cycles = 0

  index, num = get_max(bank)
  bank[index] = 0
  index += 1
  while num > 0:
      if index == len(bank):
          index = 0
      bank[index] += 1
      num -= 1
      index += 1
  cycles += 1

  while tuple(bank) != aim:
      index, num = get_max(bank)
      bank[index] = 0
      index += 1
      while num > 0:
          if index == len(bank):
              index = 0
          bank[index] += 1
          num -= 1
          index += 1
      cycles += 1

  return cycles # part 2