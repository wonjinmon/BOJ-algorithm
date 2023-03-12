# 2751 수 정렬하기 2 
import sys
a = int(sys.stdin.readline())
q =[]
for _ in range(a):
    q.append(int(sys.stdin.readline()))

for i in sorted(q):
    print(i)