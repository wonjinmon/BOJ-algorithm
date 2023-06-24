# 1874 수택 수열
N = int(input())
stack = []
result = []
i = 1
check = 0

for _ in range(N):
  num = int(input())
  while i <= num:
    stack.append(i)
    result.append('+')
    i += 1
  if stack[-1] == num:
    stack.pop()
    result.append('-')
  else:
    print('NO')
    check = 1
    break
if check == False:
  for i in result:
    print(i)
