# 2675 문자열 반복
a = int(input())

for _ in range(a):
    R,S = map(str, input().split())
    R = int(R)
    for j in range(len(S)):
        print(S[j] * R,  end='')
    print()