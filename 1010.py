# 1010 다리 놓기
N = int(input())

def factorial(a):
  if a > 1:
    return a * factorial(a - 1)
  else:
    return 1

for _ in range(N):
  e, w = map(int, input().split())
  print(factorial(w) // (factorial(w - e) * factorial(e)))