import re
import sys

ROW = 2000000
EMPTY = set()
OCCUPIED = set()

for line in sys.stdin:
  sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
  if sy == ROW:
    OCCUPIED.add(sx)
  if by == ROW:
    OCCUPIED.add(bx)
  dx, dy = abs(bx - sx), abs(by - sy)
  if (max_dist := dx + dy - abs(ROW - sy)) >= 0:
    for x in range(sx - max_dist, sx + max_dist + 1):
      EMPTY.add(x)

print(len(EMPTY - OCCUPIED))
