# 2110 공유기 설치
N,C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = houses[0]
    
    for i in range(1, N):
        print('i', i)
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]
            
    if count >= C:
        start = mid + 1
    else:
        end = mid -1
print(end)