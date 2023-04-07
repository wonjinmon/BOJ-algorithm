# 요세푸스 문제 - circular queue
a,b = map(int, input().split())
q = [i for i in range(1, a+1)]
p = 0
print("<", end= '')
while len(q) > 1:
    p = p + b
    if p > len(q):
        p = p % len(q)
        if p == 0:
            p = p + len(q)
    p = p - 1
    print(q.pop(p), end = ', ')
print(str(q.pop())+ ">")