# 1316 그룹 단어 체커

import sys


input = sys.stdin.readline

N = int(input())
result = N

for _ in range(N):
    word = input().strip()
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            result -= 1
            break

print(result)
