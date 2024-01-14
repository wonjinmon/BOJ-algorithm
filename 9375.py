import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dic = dict()
    for _ in range(n):
        _, cls = input().split()  # 어떤 종류를 입었는 지만 중요
        if cls in dic:
            dic[cls] += 1
        else:
            dic[cls] = 1
    result = 1
    for value in dic.values():
        result *= (value + 1)  # (안입는 경우 +1)
    print(result - 1)  # (아무 것도 안입는 경우 -1)
