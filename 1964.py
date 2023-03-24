# 1964 오각형, 오각형, 오각형…
n = int(input())
a1 = 5

for i in range(1,n):
    R = (7 + 3*(i-1))
    a1 += R
    if n ==1:
        a1 = 5
print(a1%45678)