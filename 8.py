import sys

MAP = [line.strip() for line in sys.stdin]

res = 0
ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
for x in range(len(MAP)):
  for y in range(len(MAP[x])):
    for dx, dy in ds:
      vis = False
      nx, ny = x, y
      while True:
        nx, ny = nx + dx, ny + dy
        if 0 <= nx < len(MAP) and 0 <= ny < len(MAP[nx]):
          if MAP[nx][ny] >= MAP[x][y]:
            break
        else:
          vis = True
          break
      if vis:
        res += 1
        break
print(res)
