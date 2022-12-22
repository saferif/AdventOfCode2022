import sys

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
TURNS = {'L': -1, 'R': 1}
MAP, MOVES = sys.stdin.read().split('\n\n')
MAP = [x.rstrip() for x in MAP.splitlines()]

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

def wrap_around(r, c, dr, dc):
  while True:
    r, c = r - dr, c - dc
    tile = get_tile(r, c)
    if tile is None or tile == ' ':
      r, c = r + dr, c + dc
      return r, c

MOVES = parse_moves(MOVES.strip())
face, row, column = 0, 0, next(i for i, v in enumerate(MAP[0]) if v == '.')

for move in MOVES:
  if move in TURNS:
    face = (face + TURNS[move]) % 4
    continue
  for _ in range(move):
    dr, dc = DIRS[face]
    nr, nc = row + dr, column + dc
    tile = get_tile(nr, nc)
    if tile is None or tile == ' ':
      nr, nc = wrap_around(nr, nc, dr, dc)
      tile = get_tile(nr, nc)
    if tile == '.':
      row, column = nr, nc
    elif tile == '#':
      continue

print(1000 * (row + 1) + 4 * (column + 1) + face)
