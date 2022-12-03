import sys

def priority(c):
  if 'a' <= c and c <= 'z':
    return ord(c) - ord('a') + 1
  return ord(c) - ord('A') + 27

ps = 0
ss = []

for line in sys.stdin:
  s = set()
  for c in line.strip():
    s.add(c)
  ss.append(s)

for i in range(len(ss) // 3):
  t = ss[3 * i] & ss[3 * i + 1] & ss[3 * i + 2]
  c = t.pop()
  ps += priority(c)

print(ps)
