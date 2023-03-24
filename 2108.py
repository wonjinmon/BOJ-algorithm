# 2108 통계학
import sys
a = int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(int(sys.stdin.readline()))

# 산술평균
avg = (round(sum(b) / a))
# 중앙값
mid = (sorted(b)[a//2])
# 범위
rng = (max(b)-min(b))

print(avg)
print(mid)
# 최빈값
from collections import Counter
c = Counter(sorted(b))
if len(c.most_common()) > 1 and c.most_common(2)[0][1] == c.most_common(2)[1][1]:
    print(c.most_common(2)[1][0])
else:
    print(c.most_common()[0][0])
print(rng)