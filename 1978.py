# 1978 소수 찾기
N = int(input())
b = list(map(int,(input().split())))
cnt = 0
for i in b:
    for j in range (2,i+1):
        if i % j == 0:
            if i == j:
                cnt += 1
            else:
                break
print(cnt)