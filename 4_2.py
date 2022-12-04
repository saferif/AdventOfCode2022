import sys

def overlaps(a, b, x, y):
  return (x <= a and a <= y) or (x <= b and b <= y) or (a <= x and x <= b) or (a <= y and y <= b)

def count(lines):
  for line in lines:
    pair = line.strip().split(',')
    elf0 = list(map(int, pair[0].split('-')))
    elf1 = list(map(int, pair[1].split('-')))
    if overlaps(elf0[0], elf0[1], elf1[0], elf1[1]):
      yield 1

print(sum(count(sys.stdin)))
