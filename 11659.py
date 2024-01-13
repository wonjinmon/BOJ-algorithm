# 11659 구간 합 구하기 4
import sys


input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum_list = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sum_list.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(sum_list[e] - sum_list[s - 1])
