# 1065 한수

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i < 100:
        cnt += 1
    else:
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            cnt += 1

print(cnt)
