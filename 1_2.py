import sys

vals = []
val = 0

for line in sys.stdin:
  line = line.strip()
  if line == "":
    vals.append(val)
    val = 0
  else:
    val += int(line)

vals.append(val)

s = sorted(vals, reverse=True)

print(sum(s[:3]))
