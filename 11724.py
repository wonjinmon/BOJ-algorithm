# 11724 연결 요소의 개수
# 파이썬은 재귀 깊이 제한이 있어 dfs를 사용하기 위해 예외 처리
# bfs로 구현하는게 나을듯

import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
cnt = 0

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        cnt += 1
print(cnt)