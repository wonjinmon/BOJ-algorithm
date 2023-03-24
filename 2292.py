# 2292 벌집
a = int(input())

n = 1
cnt = 1

while a > n:
    n += 6 * cnt
    cnt += 1
print(cnt)