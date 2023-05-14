# 2775 부녀회장이 될테야
T = int(input())
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    bottom = [i for i in range(1,n+1)] # 1층
    for _ in range(k):
        for j in range(1, n):
            bottom[j] += bottom[j-1]
    # print(bottom)
    print(bottom[-1])