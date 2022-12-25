import sys

DIGITS = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
DIGITS_REVERSED = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

def parse_snafu(num):
  res = 0
  for d in num:
    res *= 5
    res += DIGITS[d]
  return res

def to_snafu(num):
  if num == 0:
    return ''
  m = num % 5
  if m < 3:
    return to_snafu(num // 5) + DIGITS_REVERSED[m]
  else:
    return to_snafu(num // 5 + 1) + DIGITS_REVERSED[m - 5]

print(to_snafu(sum(parse_snafu(line.strip()) for line in sys.stdin)))
