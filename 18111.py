# 18111 마인크래프트 (pypy)
import sys
input = sys.stdin.readline

N, M, B = map(int, input().rstrip().split())
ground = []
for _ in range(N):
    ground += list(map(int, input().rstrip().split()))

start = min(ground)
end = max(ground)
max_height = start
min_time = sys.maxsize

for standard in range(start, end + 1):
    time = 0
    inven = B
    for g in ground:
        block = g - standard
        if block > 0:  # 블록 제거
            inven += block
            time += 2 * block
        else:  # 블록 추가
            inven += block
            time += abs(block)
    if inven < 0:
        continue
    else:
        if time <= min_time:
            max_height = standard
            min_time = time
print(min_time, max_height)