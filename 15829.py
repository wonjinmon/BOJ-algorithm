# 15829 Hashing 
# ord : 아스키 코드 값으로 반환
L = int(input())
M = 1234567891
r = 31

a = input()
result = 0

for i in range(len(a)):
    result += ((ord(a[i])-96) * (31 ** i))
print(result % M)