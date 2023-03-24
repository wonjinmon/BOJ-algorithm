# 8958 OX퀴즈
a = int(input())

for _ in range(a):
    b = list(map(str, input()))

    score = 0
    sum = 0
    for i in range(len(b)):    
        if b[i] == 'O':
            sum += 1
        else:
            sum = 0
        score += sum
    print(score)