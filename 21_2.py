import sys
from collections import namedtuple
from operator import add, mul, sub, floordiv

Op = namedtuple('Op', ['name', 'left', 'op', 'right'])

KNOWN = {}
UNKNOWN = {}
OPERATORS = {'+': add, '-': sub, '*': mul, '/': floordiv}

def compute(cur):
  if cur in KNOWN:
    return KNOWN[cur]
  if cur == 'humn':
    return None
  op = UNKNOWN[cur]
  left = compute(op.left)
  right = compute(op.right)
  if left is not None and right is not None:
    del UNKNOWN[cur]
    res = OPERATORS[op.op](left, right)
    KNOWN[cur] = res
    return res
  return None

def solve(cur):
  if cur.name == 'humn':
    return KNOWN[cur.name]
  if cur.left in UNKNOWN:
    left, right = UNKNOWN[cur.left], KNOWN[cur.right]
    if cur.op == '+':
      KNOWN[left.name] = KNOWN[cur.name] - right
    elif cur.op == '-':
      KNOWN[left.name] = KNOWN[cur.name] + right
    elif cur.op == '*':
      KNOWN[left.name] = KNOWN[cur.name] // right
    else:
      KNOWN[left.name] = KNOWN[cur.name] * right
    return solve(left)
  else:
    left, right = KNOWN[cur.left], UNKNOWN[cur.right]
    if cur.op == '+':
      KNOWN[right.name] = KNOWN[cur.name] - left
    elif cur.op == '-':
      KNOWN[right.name] = left - KNOWN[cur.name]
    elif cur.op == '*':
      KNOWN[right.name] = KNOWN[cur.name] // left
    else:
      KNOWN[right.name] = left // KNOWN[cur.name]
    return solve(right)

for line in sys.stdin:
  monkey, action = (x.strip() for x in line.split(':'))
  if monkey == 'humn':
    continue
  vals = tuple(x.strip() for x in action.split(' '))
  if len(vals) == 1:
    KNOWN[monkey] = int(vals[0])
  else:
    UNKNOWN[monkey] = Op(name=monkey, left=vals[0], right=vals[2], op=vals[1])
UNKNOWN['humn'] = Op(name='humn', left='', right='', op='')

root = UNKNOWN['root']
left = compute(root.left)
right = compute(root.right)
if left is None:
  KNOWN[root.left] = right
  ans = solve(UNKNOWN[root.left])
else:
  KNOWN[root.right] = left
  ans = solve(UNKNOWN[root.right])
print(ans)
