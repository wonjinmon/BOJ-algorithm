# 7568 덩치

N = int(input())
temp = []
for _ in range(N):
    a = list(map(int, input().split()))
    temp.append(a)
    
for i in temp:
    result = 1    
    for j in temp:
        if (i[0] < j[0] and i[1] < j[1]):
            result += 1
    print(result, end = ' ')