# 11050 이항계수1
# nCk : N! / K! * (N-K)!

a,b = map(int, input().split())

def facto(x):
    if x > 1:
        return x * facto(x-1)
    else:
        return 1
    
print(int(facto(a) / (facto(b)* facto(a-b))))