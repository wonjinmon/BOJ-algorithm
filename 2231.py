# 2231 분해합
N = input()
a = len(N) * 9
N = int(N)

pnt = N-a

result = 0

if pnt <0:
    pnt = 0
    
for i in range(pnt, N+1):
    b = list(map(int, str(i)))
    result = i + sum(b)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)