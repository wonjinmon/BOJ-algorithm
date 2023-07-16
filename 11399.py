# 11399 ATM

N = int(input())
a = sorted(list(map(int, input().split())))
result = 0

for i in range(1, N+1):
    result += sum(a[:i])
print(result)