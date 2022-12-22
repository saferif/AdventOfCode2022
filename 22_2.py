import sys

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
TURNS = {'L': -1, 'R': 1}
MAP, MOVES = sys.stdin.read().split('\n\n')
MAP = [x.rstrip() for x in MAP.splitlines()]

CUBE_SIZE = 50
CUBE_NET = ((0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0))
CUBE_ADJACENCY = {
  (0, 0): (1, 0), (0, 1): (2, 1), (0, 2): (4, 0), (0, 3): (5, 0),
  (1, 0): (3, 2), (1, 1): (2, 2), (1, 2): (0, 2), (1, 3): (5, 3),
  (2, 0): (1, 3), (2, 1): (3, 1), (2, 2): (4, 1), (2, 3): (0, 3),
  (3, 0): (1, 2), (3, 1): (5, 2), (3, 2): (4, 2), (3, 3): (2, 3),
  (4, 0): (3, 0), (4, 1): (5, 1), (4, 2): (0, 0), (4, 3): (2, 0),
  (5, 0): (3, 3), (5, 1): (1, 1), (5, 2): (0, 1), (5, 3): (4, 3),
}

def get_cube_side(r, c):
  return CUBE_NET.index((r // CUBE_SIZE, c // CUBE_SIZE))

def transfer_cube_side(r, c, face, new_face):
  if face == 0:
    x = r
  if face == 1:
    x = CUBE_SIZE - c - 1
  if face == 2:
    x = CUBE_SIZE - r - 1
  if face == 3:
    x = c

  if new_face == 0:
    return (x, 0)
  if new_face == 1:
    return (0, CUBE_SIZE - x - 1)
  if new_face == 2:
    return (CUBE_SIZE - x - 1, CUBE_SIZE - 1)
  if new_face == 3:
    return (CUBE_SIZE - 1, x)

def get_tile(r, c):
  if r < 0 or c < 0:
    return None
  try:
    return MAP[r][c]
  except IndexError:
    return None

def parse_moves(moves):
  res = []
  while moves:
    if moves[0] in TURNS:
      res.append(moves[0])
      moves = moves[1:]
      continue
    i = 0
    while i < len(moves) and moves[i].isdigit():
      i += 1
    res.append(int(moves[:i]))
    moves = moves[i:]
  return res

def wrap_around(r, c, face):
  lr, lc = r % CUBE_SIZE, c % CUBE_SIZE
  side = get_cube_side(r, c)
  new_side, new_face = CUBE_ADJACENCY[(side, face)]
  nlr, nlc = transfer_cube_side(lr, lc, face, new_face)
  i, j = CUBE_NET[new_side]
  return (new_face, nlr + i * CUBE_SIZE, nlc + j * CUBE_SIZE)

MOVES = parse_moves(MOVES.strip())
face, row, column = 0, 0, next(i for i, v in enumerate(MAP[0]) if v == '.')

for move in MOVES:
  if move in TURNS:
    face = (face + TURNS[move]) % 4
    continue
  for _ in range(move):
    dr, dc = DIRS[face]
    nf, nr, nc = face, row + dr, column + dc
    tile = get_tile(nr, nc)
    if tile is None or tile == ' ':
      nf, nr, nc = wrap_around(row, column, face)
      tile = get_tile(nr, nc)
    if tile == '.':
      face, row, column = nf, nr, nc
    elif tile == '#':
      continue

print(1000 * (row + 1) + 4 * (column + 1) + face)
