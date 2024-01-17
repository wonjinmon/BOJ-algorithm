# 15649 N과 M (1)

import sys


input = sys.stdin.readline


def solve(n, m, depth):
    if depth == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(n, m, depth + 1)
            visited[i] = False
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    visited = [False] * N
    result = []
    solve(N, M, 0)
