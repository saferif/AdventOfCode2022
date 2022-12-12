from collections import deque
import sys

DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MAP = [line.strip() for line in sys.stdin]
STEPS = [[-1 for _ in range(len(MAP[i]))] for i in range(len(MAP))]

fr, fc = 0, 0
q = deque()
for r in range(len(MAP)):
  for c in range(len(MAP[r])):
    if MAP[r][c] == 'S':
      MAP[r] = MAP[r].replace('S', 'a')
      q.append((r, c, 0))
    if MAP[r][c] == 'E':
      fr, fc = r, c
      MAP[r] = MAP[r].replace('E', 'z')

while q:
  cr, cc, step = q.popleft()
  if STEPS[cr][cc] <= step and STEPS[cr][cc] != -1:
    continue
  STEPS[cr][cc] = step
  for dr, dc in DIRS:
    nr, nc = cr + dr, cc + dc
    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and ord(MAP[nr][nc]) - ord(MAP[cr][cc]) <= 1:
      q.append((nr, nc, step + 1))

print(STEPS[fr][fc])
