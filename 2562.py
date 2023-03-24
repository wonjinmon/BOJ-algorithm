# 2562 최댓값
n = []
for i in range(9):
    n.append(int(input()))
    b = max(n)
print(max(n) , n.index(b) + 1)