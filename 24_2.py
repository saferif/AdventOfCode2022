import sys
from collections import deque, namedtuple

MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1), (0, 0))
DIRMAP = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
Blizard = namedtuple('Blizard', ['pos', 'dir'])

data = [line.strip() for line in sys.stdin]
HEIGHT = len(data)
WIDTH = len(data[0])

def move_blizard(blizard):
  nr, nc = blizard.pos[0] + blizard.dir[0], blizard.pos[1] + blizard.dir[1]
  if nr == 0:
    nr = HEIGHT - 2
  if nr == HEIGHT - 1:
    nr = 1
  if nc == 0:
    nc = WIDTH - 2
  if nc == WIDTH - 1:
    nc = 1
  return Blizard((nr, nc), blizard.dir)

START = (0, next(i for i, t in enumerate(data[0]) if t == '.'))
FINISH = (HEIGHT - 1, next(i for i, t in enumerate(data[HEIGHT - 1]) if t == '.'))
blizards = [Blizard((row, column), DIRMAP[tile]) for row in range(1, HEIGHT - 1) for column, tile in enumerate(data[row]) if tile in DIRMAP]

FORECAST = [blizards]
while True:
  new_blizards = [move_blizard(b) for b in FORECAST[-1]]
  if new_blizards != FORECAST[0]:
    FORECAST.append(new_blizards)
  else:
    break

def bfs(start, finish, init_time):
  state = (start, init_time)
  seen = set()

  q = deque([state])
  while q:
    pos, step = q.popleft()
    if pos == finish:
      return step

    step += 1
    blizard_idx = step % len(FORECAST)
    blizards = FORECAST[blizard_idx]

    if (pos, blizard_idx) in seen:
      continue
    seen.add((pos, blizard_idx))
  
    for dr, dc in MOVES:
      nr, nc = pos[0] + dr, pos[1] + dc
      if 0 <= nr < HEIGHT and 0 <= nc < WIDTH and data[nr][nc] != '#' and (nr, nc) not in map(lambda x: x.pos, blizards):
        q.append(((nr, nc), step))

t = bfs(START, FINISH, 0)
t = bfs(FINISH, START, t)
print(bfs(START, FINISH, t))
