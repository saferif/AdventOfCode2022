import sys

MINUS = ['####']
CROSS = ['.#.', '###', '.#.']
L_SHAPE = ['..#', '..#', '###']
COL = ['#', '#', '#', '#']
BOX = ['##', '##']

def cycle(it):
  while True:
    for i, v in enumerate(it):
      yield i, v

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
CACHE = {}
NUM_ROCKS = 1000000000000

def hash2(shape_idx, wind_idx, max_height):
  return (shape_idx, wind_idx, frozenset((max_height - p[0], p[1]) for p in MAP if max_height - p[0] <= 30))

max_height = 0
added_max_height = 0
rock_idx = 0
while rock_idx < NUM_ROCKS:
  shape_idx, rock = next(SHAPES)
  row = max_height + 4
  col = 3
  prev_drawn = None
  while True:
    wind_idx, wind = next(WIND)
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
  
  state = hash2(shape_idx, wind_idx, max_height)
  if (res := CACHE.get(state, None)):
    loop_length = rock_idx - res[0]
    num_loops = (NUM_ROCKS - rock_idx) // loop_length
    rock_idx += num_loops * loop_length
    added_max_height = num_loops * (max_height - res[1])
    CACHE.clear()
  else:
    CACHE[state] = (rock_idx, max_height) 
  
  rock_idx += 1

print(max_height + added_max_height)
