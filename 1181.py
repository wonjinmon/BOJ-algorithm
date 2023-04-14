# 1181 단어 정렬
N = int(input())
list1 = []
for _ in range(N):
    list1.append(input())
list1 = list(set(list1))
list1.sort()
list1.sort(key= lambda x: len(x))

for i in list1:
    print(i)