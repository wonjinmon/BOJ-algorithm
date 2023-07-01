# 2525 오븐시계
cur = list(map(int, input().split()))
time = int(input())

h = cur[0] + (time//60)
m = cur[1] + (time%60)
if m >= 60:
    m %= 60
    h+=1
if h >= 24:
    h %= 24
print(h,m)