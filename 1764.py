# 1764 듣보잡

import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())

# 듣도X + 보도X
name_list = []
for _ in range(N+M):
    name_list.append(input().rstrip())

new_list = sorted(Counter(name_list).most_common())

result = 0
for name, counts in new_list:
    if counts == 2:
        result += 1
print(result)

for name, counts in new_list:
    if counts == 2:
        print(name)
