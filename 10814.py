# 10814 나이순 정렬
N = int(input())
list1 = []
for _ in range(N):
    list1.append(list(map(str, input().split())))
list1.sort(key= lambda x: int(x[0]))
for i in range(N):
    print(list1[i][0], list1[i][1])