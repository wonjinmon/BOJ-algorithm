# 4153 직각삼각형
while True:
    a,b,c, = map(int, input().split())
    if (a + b + c == 0):
        break
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b **2):
        print('right')
    else:
        print('wrong') 