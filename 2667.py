# 2667 단지번호붙이기

import sys
from collections import deque


input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global cnt
    graph[x][y] = 0
    q = deque([(x, y)])
    while q:
        visited = q.popleft()
        for i in range(4):
            nx = visited[0] + dx[i]
            ny = visited[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1


N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 1
            bfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for r in range(len(result)):
    print(result[r])
