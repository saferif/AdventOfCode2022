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
  op = UNKNOWN[cur]
  left = compute(op.left)
  right = compute(op.right)
  return op.op(left, right)

for line in sys.stdin:
  monkey, action = (x.strip() for x in line.split(':'))
  vals = tuple(x.strip() for x in action.split(' '))
  if len(vals) == 1:
    KNOWN[monkey] = int(vals[0])
  else:
    UNKNOWN[monkey] = Op(name=monkey, left=vals[0], right=vals[2], op=OPERATORS[vals[1]])

print(compute('root'))
