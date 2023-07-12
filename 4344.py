# 4344 평균은 넘겠지

N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    threshold = (sum(a[1:]) / a[0])
    count = 0
    for i in a[1:]:
        if i > threshold:
            count += 1
    print(f"{(count / a[0])* 100:.3f}%")