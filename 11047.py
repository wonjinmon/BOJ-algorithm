# 11047 동전 0

import sys


input = sys.stdin.readline
N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input().strip()))

cnt = 0
for i in coins[::-1]:
    if K < i:
        i += 1
    elif K >= 0:
        cnt += K // i
        K %= i
    else:
        break
print(cnt)
