# 1676 팩토리얼 0의 개수  

def factorial(x):
    while x>1:
        return x * factorial(x-1)
    else:
        return 1
    
temp = factorial(int(input()))
cnt = 0
for i in str(temp)[::-1]:
    if i !='0':
        break
    cnt += 1
print(cnt)