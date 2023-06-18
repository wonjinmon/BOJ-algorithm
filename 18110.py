# 18110 solved.ac
import sys
from collections import deque
def my_round(x):
    return int(x) + 1 if x - int(x) >= 0.5 else int(x)

N = int(sys.stdin.readline())

level = []

for _ in range(N):
    level.append(int(sys.stdin.readline()))
if N == 0:
    print(0)
else:
    delete = my_round(N * 0.15)
    level.sort()
    level = deque(level)
    for _ in range(delete):
        level.pop()
        level.popleft()
    print(my_round(sum(level) / (N - 2*delete)))