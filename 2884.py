# 2884 알람 시계 
h, m = map(int, input().split()) 
if (m-45) < 0:
    m = (m-45) + 60
    h -= 1
    if h == -1:
        h = 23
else:
    m = m- 45
print(h,m)