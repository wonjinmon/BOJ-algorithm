# 17219 비밀번호 찾기

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()

for _ in range(N):
    address, password = input().split()
    dic[address] = password

for _ in range(M):
    find = input().strip()
    if find in dic.keys():
        print(dic[find])
