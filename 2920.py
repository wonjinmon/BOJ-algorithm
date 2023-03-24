# 2920 음계
a = list(map(int, input().split()))

asc = [1,2,3,4,5,6,7,8]
des = sorted(asc ,reverse=True)

if a == asc:
    print('ascending')
elif a == des:
    print('descending')
else:
    print('mixed')