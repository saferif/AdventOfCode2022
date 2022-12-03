import sys

def priority(c):
  if 'a' <= c and c <= 'z':
    return ord(c) - ord('a') + 1
  return ord(c) - ord('A') + 27

def check(line):
  s = set()
  for c in line[:len(line)//2]:
    s.add(c)
  for c in line[len(line)//2:]:
    if c in s:
      return priority(c)

ps = 0

for line in sys.stdin:
  ps += check(line.strip())

print(ps)
