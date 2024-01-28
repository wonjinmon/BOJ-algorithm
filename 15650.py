# 15650 N과 M (2)

import sys


input = sys.stdin.readline


def solve(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            solve(i + 1)
            result.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    result = []
    solve(1)
