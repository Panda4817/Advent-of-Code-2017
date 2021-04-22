def part1(data):
  nums = [int(n) for n in data]
  total = 0
  for i in range(len(data) - 1):
    if nums[i] == nums[i + 1]:
      total += nums[i]
  
  if nums[-1] == nums[0]:
    total += nums[-1]
  
  return total

def part2(data):
  nums = [int(n) for n in data]
  total = 0
  h = len(nums) // 2
  for i in range(len(data)):
    try:
      if nums[i] == nums[i + h]:
        total += nums[i]
    except IndexError:
      diff = h - (len(nums) - i)
      if nums[i] == nums[diff]:
        total += nums[i]
  
  return total