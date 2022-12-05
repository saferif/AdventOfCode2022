import re
import sys
from collections import deque

lines = [line for line in sys.stdin]

def read_crates(lines):
  crates = []
  lines_processed = 0
  for line in lines:
    lines_processed += 1
    i = 0
    newcrate = False
    while 4 * i < len(line):
      if len(crates) <= i:
        crates.append(deque())
      crate = line[4 * i:4 * i + 4]
      if crate[0] == '[':
        crates[i].append(crate[1])
        newcrate = True
      i += 1
    if not newcrate:
      break
  return lines[lines_processed+1:], crates

lines, crates = read_crates(lines)
for line in lines:
  m = re.search('move (\d+) from (\d+) to (\d+)', line)
  if m:
    n = int(m.group(1))
    x = int(m.group(2)) - 1
    y = int(m.group(3)) - 1
    e = []
    for i in range(n):
      e.append(crates[x].popleft())
    crates[y].extendleft(e)

print(''.join(crate[0] for crate in crates))
