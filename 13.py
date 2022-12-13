import sys

PACKETS = [[eval(line) for line in pair.split('\n')] for pair in sys.stdin.read().strip().split('\n\n')]

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

print(sum((i + 1 for i, p in enumerate(PACKETS) if compare(p[0], p[1]) < 0)))
