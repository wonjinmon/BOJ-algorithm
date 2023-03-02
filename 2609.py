# 2609 최대공약수와 최소공배수 - 유클리드 호제법
a,b = map(int, input().split())

def GCD(a,b):
  while b>0:
    a,b = b, a % b
  return a
print(GCD(a,b))

LCM = a * b // GCD(a,b)
print(LCM)