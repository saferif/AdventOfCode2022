import sys

MINUS = ['####']
CROSS = ['.#.', '###', '.#.']
L_SHAPE = ['..#', '..#', '###']
COL = ['#', '#', '#', '#']
BOX = ['##', '##']

def cycle(it):
  while True:
    for i in it:
      yield i

def draw(shape, row, col):
  for i in range(len(shape)):
    for j in range(len(shape[i])):
      if shape[len(shape) - i - 1][j] == '#':
        yield (row + i, col + j)

def width_fits(shape, col):
  return not (col < 1 or col + len(shape[0]) - 1 > 7)

MAP = set()
WIND = cycle(sys.stdin.read().strip())
SHAPES = cycle((MINUS, CROSS, L_SHAPE, COL, BOX))

max_height = 0
for _ in range(2022):
  rock = next(SHAPES)
  row = max_height + 4
  col = 3
  prev_drawn = None
  while True:
    wind = next(WIND)
    if wind == '<' and width_fits(rock, col - 1) and len((drawn := set(draw(rock, row, col - 1))) & MAP) == 0:
      col -= 1
      prev_drawn = drawn
    elif wind == '>' and width_fits(rock, col + 1) and len((drawn := set(draw(rock, row, col + 1))) & MAP) == 0:
      col += 1
      prev_drawn = drawn
    
    row -= 1
    drawn = set(draw(rock, row, col))
    if row < 1 or len(drawn & MAP) > 0:
      max_height = max(max_height, *(p[0] for p in prev_drawn))
      MAP.update(prev_drawn)
      break
    else:
      prev_drawn = drawn

print(max_height)
