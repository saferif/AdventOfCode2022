import sys

X = [0, 1]

for line in sys.stdin:
    toks = line.split()
    X.append(X[-1])
    if toks[0] == 'addx':
      X.append(X[-1] + int(toks[1]))
print(sum(X[i]*i for i in range(20, 221, 40)))
