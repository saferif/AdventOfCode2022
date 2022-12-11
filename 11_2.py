import re
import sys

data = sys.stdin.read().split('\n\n')

class Monkey(object):
  def __init__(self, items, operation, test):
    self.items = items
    self.operation = operation
    self.test = test
    self.count = 0

monkeys = {}

cm = 1
for block in data:
  lines = block.split('\n')
  ID = int(re.findall(r'\d+', lines[0])[0])
  items = list(map(int, re.findall(r'\d+', lines[1])))
  operation = lines[2].split('=')[1].strip()
  q = int(re.findall(r'\d+', lines[3])[0])
  t = int(re.findall(r'\d+', lines[4])[0])
  f = int(re.findall(r'\d+', lines[5])[0])
  monkeys[ID] = Monkey(items, operation, [f, t, q])
  cm *= q

for _ in range(10000):
  for i in sorted(monkeys.keys()):
    for item in monkeys[i].items:
      monkeys[i].count += 1
      item = eval(monkeys[i].operation, {}, {'old': item}) % cm
      nextID = monkeys[i].test[int(item % monkeys[i].test[2] == 0)]
      monkeys[nextID].items.append(item)
    monkeys[i].items.clear()

t = sorted(map(lambda m: m.count, monkeys.values()))
print(t[-1] * t[-2])
