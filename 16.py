import re
import sys

MAX_TIME = 30

TUNNELS = {}
FLOW = {}

def dfs(room, open_valves, visited, flow, elapsed):
  if elapsed == MAX_TIME:
    return flow
  if (room, flow) in visited:
    return flow
  
  max_flow = flow
  new_visited = visited | set([(room, flow)])
  if room not in open_valves and FLOW[room] > 0:
    max_flow = max(max_flow, dfs(room, open_valves | set([room]), new_visited, flow + (MAX_TIME - (elapsed + 1)) * FLOW[room], elapsed + 1))
  for tunnel in TUNNELS[room]:
    max_flow = max(max_flow, dfs(tunnel, open_valves, new_visited, flow, elapsed + 1))
  return max_flow

for line in sys.stdin:
  m = re.search(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
  valve = m.group(1)
  flow = int(m.group(2))
  tunnels = [t.strip() for t in m.group(3).split(',')]
  TUNNELS[valve] = tunnels
  FLOW[valve] = flow

print(dfs('AA', set(), set(), 0, 0))
