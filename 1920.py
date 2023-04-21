# 1920 수 찾기
import sys
N = int(sys.stdin.readline())
Nlist = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))
for i in Mlist:
    print(1) if i in Nlist else print(0)

# Nlist를 세트로 해야 시간 초과 x
# set의 시간복잡도 O(1), list의 시간복잡도 O(n)