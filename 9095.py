# 9095 1,2,3 더하기
import sys
input = sys.stdin.readline

def my_function(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return my_function(x-1) + my_function(x-2) + my_function(x-3)

T = int(input())

for _ in range(T):
    n = int(input())
    print(my_function(n))