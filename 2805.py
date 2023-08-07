# 2805 나무 자르기
N, M = map(int, input().split())

trees= list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    h = 0
    for tree in trees:
        if tree > mid: 
            h += (tree - mid)
    if h >= M:
        start = mid +1
    else:
        end = mid - 1
print(end)