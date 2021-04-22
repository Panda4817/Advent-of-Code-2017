# Part2 in part1
def part1(data):
  def unique_words(l):
    for i in range(len(l)):
      if l[i] in l[0:i] + l[i+1:]:
        return False
      for j in range(i + 1, len(l)):
        if are_anagrams(l[i], l[j]):
          return False
    return True
  
  def are_anagrams(w1, w2):
    if len(w1) != len(w2):
      return False
    sorted_w1 = sorted(list(w1))
    sorted_w2 = sorted(list(w2))
    if "".join(sorted_w1) != "".join(sorted_w2):
      return False
    
    return True
  
  lst = [l.split() for l in data.split("\n")]
  valid = 0
  for l in lst:
    if unique_words(l):
      valid += 1
  return valid

      
