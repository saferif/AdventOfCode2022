import sys

WIDTH = 40
HEIGHT = 6
X = [0, 1]

for line in sys.stdin:
    toks = line.split()
    X.append(X[-1])
    if toks[0] == 'addx':
      X.append(X[-1] + int(toks[1]))

for y in range(HEIGHT):
  for x in range(WIDTH):
    cycle = y * WIDTH + x + 1
    if abs(x - X[cycle]) <= 1:
      print('#', end='')
    else:
      print('.', end='')
  print()
