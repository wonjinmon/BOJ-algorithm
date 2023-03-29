# 1929 소수 구하기  
# int(pow(i, 0.5)를 하는 이유는 최대 약수가 sqrt(n) 이하 // i+1까지로 범위 설정시 시간초과
# 12 = 1*12,  2*6,  3*4,  4*3,  6*2,  12*1
# 2 or 3이 결정
a,b = map(int, input().split())

for i in range(a, b + 1):
    n = 1
    for j in range( 2, int(pow(i, 0.5) + 1)):
        if i % j == 0:
            n = 0
            break
    if n == 1 and i != 1:
        print(i)

# 에라토스테네스의 체
M , N = map(int,input().split())

r = N + 100

cheak = [False for _ in range(r)]

for i in range( 2, int(r**0.8) ) : 
    if cheak[i] == False : 
        for j in range( i*2 , r, i ): 
            cheak[j] = True

prime_number = [i for i,j in enumerate(cheak) if i>=2 and j==False]

for i in prime_number:
    if N >= i >= M:
        print(i)