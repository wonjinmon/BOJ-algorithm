# 2606 바이러스
import sys
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    global cnt
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

cnt = 0
dfs(1)
print(cnt)