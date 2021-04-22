def part1(data):
  spreadsheet = [[int(i) for i in r.split()] for r in data.split("\n")]
  diffs = [max(row) - min(row) for row in spreadsheet]
  return sum(diffs)

def part2(data):
  spreadsheet = [[int(i) for i in r.split()] for r in data.split("\n")]
  divisibles = []
  for row in spreadsheet:
    for i in range(len(row)):
      for j in range(i + 1, len(row)):
        if row[i] % row[j] == 0:
          divisibles.append(row[i] // row[j])
        elif row[j] % row[i] == 0:
          divisibles.append(row[j] // row[i])
  return sum(divisibles)

  
