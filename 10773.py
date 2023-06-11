# 10773 제로
from collections import deque
K = int(input())
q = deque()

for _ in range(K):
    num = int(input())
    if num != 0:
        q.append(num)
    else:
        q.pop()
print(sum(q))