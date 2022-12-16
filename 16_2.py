import re
import sys
from functools import cache

MAX_TIME = 26

TUNNELS = {}
FLOW = {}
IDXS = {}

def is_valve_open(open_valves, valve):
  idx = IDXS[valve]
  return (open_valves & (1 << idx)) > 0

def open_valve(open_valves, valve):
  idx = IDXS[valve]
  return open_valves | (1 << idx)

def finish(open_valves, elephant):
  if not elephant:
    return dfs('AA', open_valves, 0, True)
  return 0

@cache
def dfs(room, open_valves, elapsed, elephant):
  if elapsed == MAX_TIME:
    return finish(open_valves, elephant)
  
  max_flow = 0
  if not is_valve_open(open_valves, room) and FLOW[room] > 0:
    max_flow = max(max_flow, dfs(room, open_valve(open_valves, room), elapsed + 1, elephant) + (MAX_TIME - (elapsed + 1)) * FLOW[room])
  for tunnel in TUNNELS[room]:
    max_flow = max(max_flow, dfs(tunnel, open_valves, elapsed + 1, elephant))
  return max_flow

for line in sys.stdin:
  m = re.search(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
  valve = m.group(1)
  flow = int(m.group(2))
  tunnels = [t.strip() for t in m.group(3).split(',')]
  TUNNELS[valve] = tunnels
  FLOW[valve] = flow
  IDXS[valve] = len(IDXS)

print(dfs('AA', 0, 0, False))
