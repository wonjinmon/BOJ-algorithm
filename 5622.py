# 5622 다이얼

import sys


input = sys.stdin.readline

word = input()
result = 0

for i in word:
    if i in 'ABC':
        result += 3
    elif i in 'DEF':
        result += 4
    elif i in 'GHI':
        result += 5
    elif i in 'JKL':
        result += 6
    elif i in 'MNO':
        result += 7
    elif i in 'PQRS':
        result += 8
    elif i in 'TUV':
        result += 9
    elif i in 'WXYZ':
        result += 10
print(result)
