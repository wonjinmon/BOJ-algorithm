# 1712 손익분기점
a,b,c = map(int, input().split())

if c-b > 0:
    bp = a // (c-b) + 1
    print(bp)
else:
    print(-1)