# 2798 블랙잭 (브루트 포스)
N,M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = nums[i] + nums[j] + nums[k]
            if result < temp <= M:
                result = temp
print(result)