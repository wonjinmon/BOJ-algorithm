# 2579 계단 오르기
import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * 301
dp = [0] * 301
for i in range(N):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max((stairs[0] + stairs[2]), (stairs[1] + stairs[2]))

for i in range(3, N + 1):
    dp[i] = max((stairs[i] + dp[i - 2]), (stairs[i] + stairs[i - 1] + dp[i - 3]))
print(dp[N - 1])