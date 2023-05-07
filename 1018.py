N,M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())
count = []

# N*M 보드에서 경우의 수 N-i * M-j
for i in range(N-7):
    for j in range(M-7):
        first_B = 0 # black으로 시작할때 바꿔야할 체스판 수
        first_W = 0 # white으로 시작할때 바꿔야할 체스판 수
        for k in range(i,i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: # 인덱스의 합이 짝수인지 홀수인지로 체크무늬 판단 가능
                    if board[k][l] != 'W':
                        first_B += 1
                    if board[k][l] != 'B':
                        first_W += 1
                else:
                    if board[k][l] != 'B':
                        first_B += 1
                    if board[k][l] != 'W':
                        first_W += 1
        count.append(first_W)
        count.append(first_B)
print(min(count))