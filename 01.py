import sys

maxval = 0
val = 0

for line in sys.stdin:
  line = line.strip()
  if line == "":
    maxval = max(maxval, val)
    val = 0
  else:
    val += int(line)

print(max(maxval, val))
