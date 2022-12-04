import sys

def contained(a, b, x, y):
  return (a <= x and y <= b) or (x <= a and b <= y)

def count(lines):
  for line in lines:
    pair = line.strip().split(',')
    elf0 = list(map(int, pair[0].split('-')))
    elf1 = list(map(int, pair[1].split('-')))
    if contained(elf0[0], elf0[1], elf1[0], elf1[1]):
      yield 1

print(sum(count(sys.stdin)))
