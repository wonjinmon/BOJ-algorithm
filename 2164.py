# 2164 카드2
from collections import deque
N = int(input())
a = deque(i for i in range(1, N+1))
while len(a) > 1:
    a.popleft()
    a.append(a[0])
    a.popleft()
print(a.pop())