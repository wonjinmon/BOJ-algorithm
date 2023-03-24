# 10250 ACM 호텔
t = int(input())

for _ in range(t):
    h,w,n = map(int, input().split())

    cng = n % h
    ho = n // h + 1

    if n % h == 0:
        cng = h
        ho = n // h

    print(cng*100 + ho)