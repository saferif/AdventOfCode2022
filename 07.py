import sys

class Node(object):
  def __init__(self, parent, name, isdir=False, size=0):
    self.parent = parent
    self.name = name
    self.isdir = isdir
    self.size = size
    self.children = []

  def update_size(self):
    self.size = sum(x.size for x in self.children)
    if self.parent:
      self.parent.update_size()

root = Node(None, '/', isdir=True)

def dir_sizes(t):
  yield t.size
  for c in t.children:
    if c.isdir:
      yield from dir_sizes(c)

cur = None

for line in sys.stdin:
  toks = line.split()
  if toks[0] == '$':
    if toks[1] == 'cd':
      if toks[2] == '/':
        cur = root
      elif toks[2] == '..':
        cur = cur.parent
      else:
        cur = next(filter(lambda x: x.isdir and x.name == toks[2], cur.children))
  elif toks[0] == 'dir':
    cur.children.append(Node(cur, toks[1], isdir=True))
  else:
    cur.children.append(Node(cur, toks[1], size=int(toks[0])))
    cur.update_size()

print(sum(s for s in dir_sizes(root) if s <= 100000))
