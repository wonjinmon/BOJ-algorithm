from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):

    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[N-1][M-1]


N, M = map(int, input().split())
graph = []

for _ in range(N):
    a = list(map(int, input().rstrip()))
    graph.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))