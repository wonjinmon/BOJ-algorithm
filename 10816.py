# 10816 숫자 카드 2
from collections import Counter
import sys

N = int(sys.stdin.readline())
Nlist = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))

c = Counter(Nlist)
for i in Mlist:
    print(c[i], end=' ') if i in c else print(0, end=' ')