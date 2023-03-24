# 5789 한다 안한다
N = int(input())

for i in range(N):
    numbers = input()
    idx = len(numbers) // 2  - 1
    if numbers[idx] == numbers[idx + 1]:
        print('Do-it')
    else:
        print('Do-it-Not')