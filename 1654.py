# 1654 랜선 자르기 - 이분 탐색

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
lines = sorted(lines)

start, end = 1, max(lines)
while start <= end:
    mid = (start + end) // 2
    num_lines = 0
    for line in lines:
        num_lines += line // mid
    if num_lines >= N:
        start = mid +1
    else:
        end = mid - 1
print(end)