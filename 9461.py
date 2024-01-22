# 9461 파도반 수열

import sys


input = sys.stdin.readline

triangle = [0] * 101

triangle[1] = 1
triangle[2] = 1
triangle[3] = 1

for i in range(4, 101):
    triangle[i] = triangle[i - 2] + triangle[i - 3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(triangle[N])
