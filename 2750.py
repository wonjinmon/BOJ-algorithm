# 2750 수 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
for i in sorted(num_list):
    print(i)
