import sys

SHAPE = set((x, y, z) for x, y, z in (map(int, line.strip().split(',')) for line in sys.stdin))
DIRS = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

print(sum(len(n - SHAPE) for n in (set((p[0] + d[0], p[1] + d[1], p[2] + d[2]) for d in DIRS) for p in SHAPE)))
