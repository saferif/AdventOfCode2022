import re
import sys
from functools import cache

MAX_TIME = 32

def try_make_robot(resources, robot_cost):
  final = [0 for _ in range(len(resources))]
  for i in range(len(robot_cost)):
    if resources[i] < robot_cost[i]:
      return None
    final[i] = resources[i] - robot_cost[i]
  return tuple(final)

def is_robot_needed(idx, robots, robot_costs):
  if idx == 3:
    return True
  return robots[idx] < max(rc[idx] for rc in robot_costs)

def drop_excess(resources, robot_costs, time_left):
  final = [v for v in resources]
  for i in range(len(resources) - 1):
    can_spend = time_left * max(rc[i] for rc in robot_costs)
    final[i] = min(final[i], can_spend)
  return tuple(final)

EMPTY_RESOURCES = (0, 0, 0, 0)

add_resources = lambda a, b: tuple(v1 + v2 for v1, v2 in zip(a, b))
add_robot = lambda idx, robots: tuple(v + 1 if i == idx else v for i, v in enumerate(robots))
max_resource = lambda a, b: max(a, b, key=lambda x: x[3])

@cache
def dfs(resources, robots, robot_costs, time_left):
  if time_left == 0:
    return resources

  max_resources = EMPTY_RESOURCES
  
  robot_types_available = 0
  for i in range(len(robot_costs)):
    if not is_robot_needed(i, robots, robot_costs):
      continue
    new_resources = try_make_robot(resources, robot_costs[i])
    if new_resources is not None:
      robot_types_available += 1
      new_robots = add_robot(i, robots)
      new_resources = add_resources(new_resources, robots)
      new_resources = drop_excess(new_resources, robot_costs, time_left - 1)
      new_resources = dfs(new_resources, new_robots, robot_costs, time_left - 1)
      max_resources = max_resource(max_resources, new_resources)

  if robot_types_available < len(robot_costs):
    new_resources = add_resources(resources, robots)
    new_resources = drop_excess(new_resources, robot_costs, time_left - 1)
    new_resources = dfs(new_resources, robots, robot_costs, time_left - 1)
    max_resources = max_resource(max_resources, new_resources)

  return max_resources

res = []
for line in sys.stdin:
  if len(res) == 3:
    break
  robot_costs = [None, None, None, None]
  nums = re.findall(r'\d+', line)
  blueprint_id = int(nums[0])
  robot_costs[0] = (int(nums[1]), 0, 0, 0)            # ore
  robot_costs[1] = (int(nums[2]), 0, 0, 0)            # clay
  robot_costs[2] = (int(nums[3]), int(nums[4]), 0, 0) # obsidian
  robot_costs[3] = (int(nums[5]), 0, int(nums[6]), 0) # geode

  resources = dfs(EMPTY_RESOURCES, (1, 0, 0, 0), tuple(robot_costs), MAX_TIME)
  res.append(resources[3])

print(res[0] * res[1] * res[2])
