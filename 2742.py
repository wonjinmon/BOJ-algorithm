# 기찍 N

a = int(input())

val = []
for i in range(1,a+1):
    val.append(i)
for v in range(len(val)):
    print(val.pop())
