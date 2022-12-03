import sys

TURNS = {
  'A': 1,
  'X': 1,
  'B': 2,
  'Y': 2,
  'C': 3,
  'Z': 3,
}

def round(my, other):
  if my == other:
    return 3
  if my == 2 and other == 1:
    return 6
  if my == 3 and other == 2:
    return 6
  if my == 1 and other == 3:
    return 6
  return 0

score = 0

for line in sys.stdin:
  step = line.strip().split(' ')
  other = TURNS[step[0]]
  my = TURNS[step[1]]
  score += round(my, other) + my

print(score)
