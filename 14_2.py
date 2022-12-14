import sys

PATHS = [[tuple(map(int,p.strip().split(','))) for p in line.strip().split('->')] for line in sys.stdin]

my = 0
blocked = set()
for path in PATHS:
  for i in range(1, len(path)):
    a1, b1 = min(path[i - 1][0], path[i][0]), max(path[i - 1][0], path[i][0])
    for x in range(a1, b1 + 1):
      a2, b2 = min(path[i - 1][1], path[i][1]), max(path[i - 1][1], path[i][1])
      for y in range(a2, b2 + 1):
        blocked.add((x, y))
        my = max(my, y)

count = 0
def dfs(x, y):
  global count
  if y == my + 2:
    return
  if (x, y) in blocked:
    return
  count += 1
  blocked.add((x, y))
  dfs(x, y + 1)
  dfs(x - 1, y + 1)
  dfs(x + 1, y + 1)

dfs(500, 0)
print(count)
