# 10866 덱
import sys
from collections import deque
q = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        q.appendleft(command[1])
    if command[0] == 'push_back':
        q.append(command[1])
    if command[0] == 'pop_front':
        if len(q) == 0: print(-1)
        else: print(q.popleft())
    if command[0] == 'pop_back':
        if len(q) == 0: print(-1)
        else: print(q.pop())
    if command[0] == 'size':
        print(len(q))
    if command[0] == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    if command[0] == 'front':
        if len(q) == 0: print(-1)
        else: print(q[0])
    if command[0] == 'back':
        if len(q) == 0: print(-1)
        else: print(q[-1])