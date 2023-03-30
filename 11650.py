# 11650 좌표 정렬하기
N = int(input())
list1 = []
for _ in range(N):
    list1.append(list(map(int, input().split())))
list1 = sorted(list1)
for i in range((N)):
    print(list1[i][0], list1[i][1])