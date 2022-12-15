import re
import sys
from collections import defaultdict

MAX_COORD = 4000000

def clamp(p):
  a = max(p[0], 0)
  b = min(p[1], MAX_COORD)
  return (a, b) if a <= b else None

YS = defaultdict(list)

for line in sys.stdin:
  sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
  dx, dy = abs(sx - bx), abs(sy - by)
  dist = dx + dy
  for y in range(sy - dist, sy + dist + 1):
    if not (0 <= y <= MAX_COORD):
      continue
    delta = dist - abs(sy - y)
    if (new := clamp((sx - delta, sx + delta))):
      YS[y].append(new)

for y, ranges in YS.items():
  ranges.sort()
  m = ranges[0]
  for i in range(1, len(ranges)):
    if m[1] + 1 < ranges[i][0]:
      print((m[1] + 1) * 4000000 + y)
      break
    else:
      m = (m[0], max(m[1], ranges[i][1]))
  else:
    continue
  break
