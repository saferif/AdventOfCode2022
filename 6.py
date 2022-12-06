import sys

line = sys.stdin.buffer.read().decode('utf-8').strip()

window = lambda s, size: (s[i:i + size] for i in range(len(s) - size + 1))

WINDOW_SIZE = 4

x = (i + WINDOW_SIZE for i, s in enumerate(window(line, WINDOW_SIZE)) if len(s) == len(set(c for c in s)))
print(next(x))
