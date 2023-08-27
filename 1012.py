# 1012 유기농 배추
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향 지정
    for dx, dy in directions: 
        nx, ny = dx + x, dy + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
        result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)
