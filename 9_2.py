import sys

DIRS = {
  'R': (1, 0),
  'U': (0, -1),
  'L': (-1, 0),
  'D': (0, 1),
}
POS = set()
KNOTS = 10
ROPE = [(0, 0) for _ in range(KNOTS)]

def sign(x):
  if x < 0:
    return -1
  if x > 0:
    return 1
  return 0

for line in sys.stdin:
  toks = line.split()
  dx, dy = DIRS[toks[0]]
  for _ in range(int(toks[1])):
    ROPE[0] = (ROPE[0][0] + dx, ROPE[0][1] + dy)
    for i in range(1, len(ROPE)):
      mx, my = ROPE[i-1][0] - ROPE[i][0], ROPE[i-1][1] - ROPE[i][1]
      if abs(mx) > 1 or abs(my) > 1:
        ROPE[i] = (ROPE[i][0] + sign(mx), ROPE[i][1] + sign(my))
    POS.add(ROPE[-1])
print(len(POS))
