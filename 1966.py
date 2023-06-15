# 1966 프린터 큐 
from collections import deque
T  = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    importance = deque(map(int, input().split()))
    idx = deque(range(N))
    cnt = 0

    while importance:
        if importance[0] == max(importance):
            importance.popleft()
            cnt += 1

            if idx.popleft() == M:
                print(cnt)
        else:
            importance.append(importance.popleft())
            idx.append(idx.popleft())
