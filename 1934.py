# 1934 최소공배수
import sys
input = sys.stdin.readline

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    LCM = A * B // GCD(A, B)
    print(LCM)