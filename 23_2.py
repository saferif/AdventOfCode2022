import sys

ELFS = set()
ALL_ADJACENT = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
DIRS = [((-1, 0), (-1, 1), (-1, -1), (-1, 0)), ((1, 0), (1, 1), (1, -1), (1, 0)), ((0, -1), (-1, -1), (1, -1), (0, -1)), ((0, 1), (-1, 1), (1, 1), (0, 1))]

row = 0
for line in sys.stdin:
  for column, tile in enumerate(line.strip()):
    if tile == '#':
      ELFS.add((row, column))
  row += 1    

ans = 0
while True:
  ans += 1
  proposals = {}
  clashes = set()
  for (elfr, elfc) in ELFS:
    for (dr, dc) in ALL_ADJACENT:
      if (elfr + dr, elfc + dc) in ELFS:
        break
    else:
      continue

    for dirset in DIRS:
      for (dr, dc) in dirset[:3]:
        if (elfr + dr, elfc + dc) in ELFS:
          break
      else:
        pr = dirset[3]
        new = (elfr + pr[0], elfc + pr[1])
        if new not in proposals:
          proposals[new] = (elfr, elfc)
        else:
          clashes.add(new)
        break

  t = DIRS[0]
  DIRS = DIRS[1:]
  DIRS.append(t)

  if not proposals and not clashes:
    break

  for clash in clashes:
    del proposals[clash]

  for proposal in proposals:
    ELFS.remove(proposals[proposal])
    ELFS.add(proposal)

print(ans)
