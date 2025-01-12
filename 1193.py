# 1193 분수찾기

import sys
input = sys.stdin.readline

N = int(input())
line = 1

# 위치 찾기
while N > line:
    N -= line
    line += 1

# 짝수 줄
if line % 2 == 0:
    a = N
    b = line - N + 1

# 홀수 줄
elif line % 2 == 1:
    a = line - N + 1
    b = N

print(f'{a}/{b}')
