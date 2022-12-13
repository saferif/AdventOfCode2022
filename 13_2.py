import sys
from functools import cmp_to_key

DIVIDERS = [[[2]], [[6]]]
PACKETS = [eval(line) for line in sys.stdin.read().split('\n') if line != ""] + DIVIDERS

def compare(a, b):
  if isinstance(a, int) and isinstance(b, int):
    return a - b
  if isinstance(a, list) and isinstance(b, list):
    for i in range(min(len(a), len(b))):
      c = compare(a[i], b[i])
      if c != 0:
        return c
    return len(a) - len(b)
  if isinstance(a, int):
    return compare([a], b)
  return compare(a, [b])

d1, d2 = (i + 1 for i, p in enumerate(sorted(PACKETS, key=cmp_to_key(compare))) if p in DIVIDERS)
print(d1 * d2)
