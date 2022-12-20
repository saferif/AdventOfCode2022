import sys
from math import copysign

mod = lambda a, n: int(copysign(abs(a) % n, a))

def swap(current_by_original, original_by_current, data, i, j):
  original_i = original_by_current[i]
  original_j = original_by_current[j]
  current_by_original[original_i] = j
  current_by_original[original_j] = i
  original_by_current[i] = original_j
  original_by_current[j] = original_i
  
  t = data[i]
  data[i] = data[j]
  data[j] = t

def cycle(current_by_original, original_by_current, data, i, n):
  d = int(copysign(1, n))
  while n != 0:
    ni = i + d
    if ni == -1:
      ni = len(data) - 1
    elif ni == len(data):
      ni = 0
    swap(current_by_original, original_by_current, data, i, ni)
    i = ni
    n -= d

data = [int(v) for v in sys.stdin.read().splitlines()]
current_by_original = [i for i in range(len(data))]
original_by_current = [i for i in range(len(data))]

n = len(data)
for moved in range(n):
  i = current_by_original[moved]
  x = data[i]
  delta = mod(x, n - 1)
  cycle(current_by_original, original_by_current, data, i, delta)
  moved += 1

coords = []
zero = data.index(0)
for i in (1000, 2000, 3000):
  coords.append(data[(zero + i) % n])
print(sum(coords))
