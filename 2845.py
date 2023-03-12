# 파티가 끝나고 난 뒤

l, p = map(int, input().split())
num = l * p
a = list(map(int,input().split()))
for i in a:
    print(i - num, end =' ')