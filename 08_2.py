import sys

MAP = [line.strip() for line in sys.stdin]

def score(x, y):
  res = 1
  ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
  for dx, dy in ds:
    cur = 0
    nx, ny = x, y
    while True:
      nx, ny = nx + dx, ny + dy
      if 0 <= nx < len(MAP) and 0 <= ny < len(MAP[nx]):
        cur += 1
        if MAP[nx][ny] >= MAP[x][y]:
          break
      else:
        break
    res *= cur
  return res

print(max(score(x, y) for x in range(len(MAP)) for y in range(len(MAP[x]))))
