# 2839 설탕배달
N = int(input())
count = 0

while N >= 0:
    if N % 5 ==0:
        count +=  N // 5
        print(count)
        break
    N -= 3  # 5의 배수가 될때까지 뺀다
    count +=1
else:
    print(-1)