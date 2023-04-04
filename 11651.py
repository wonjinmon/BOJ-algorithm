# 11651 좌표정렬하기 2
N= int(input())
list1 = []

for _ in range(N):
    list1.append(list(map(int, input().split())))
list1.sort(key=lambda x: x[0])
list1.sort(key=lambda x: x[1])
for i in range(N):
    print(list1[i][0], list1[i][1])