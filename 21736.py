# 21736 헌내기는 친구가 필요해

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx >= N or ny >= M or nx < 0 or ny < 0:
            continue
        if graph[nx][ny] not in ('O', 'P'):
            continue
        if graph[nx][ny] == 'P':
            global count
            count += 1
        graph[nx][ny] = 'X' # 이전에 방문한 위치 방문하지 않도록 (visted 기능)
        DFS(nx, ny)

N, M = map(int, input().split())

graph = []
start_point = ()
for x in range(N):
    a = list(input())
    graph.append(a)
    for y in range(M):
        if a[y] == 'I':
            start_point = (x, y)
        
count = 0
DFS(start_point[0], start_point[1])
print('TT' if count == 0 else count)
