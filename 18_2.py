import sys

SHAPE = set((x, y, z) for x, y, z in (map(int, line.strip().split(',')) for line in sys.stdin))
DIRS = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

nighbours = lambda p: set((p[0] + d[0], p[1] + d[1], p[2] + d[2]) for d in DIRS)

MINX, MAXX = min(p[0] for p in SHAPE), max(p[0] for p in SHAPE)
MINY, MAXY = min(p[1] for p in SHAPE), max(p[1] for p in SHAPE)
MINZ, MAXZ = min(p[2] for p in SHAPE), max(p[2] for p in SHAPE)

in_box = lambda p: (MINX - 1 <= p[0] <= MAXX + 1) and (MINY - 1 <= p[1] <= MAXY + 1) and (MINZ - 1 <= p[2] <= MAXZ + 1)

CACHE = {}

def dfs(start, seen):
  stack = [start]
  while stack:
    p = stack.pop()
    if p in seen or p in SHAPE:
      continue
    seen.add(p)
    if (not in_box(p)) or p in CACHE:
      continue
    for n in nighbours(p):
      stack.append(n)

for p in SHAPE:
  for n in nighbours(p):
    seen = set()
    dfs(n, seen)
    coolable = any(map(lambda p: (not in_box(p)) or CACHE.get(p, False), seen))
    CACHE.update({p: coolable for p in seen})
print(sum(1 for p in SHAPE for n in nighbours(p) if CACHE.get(n, False)))
