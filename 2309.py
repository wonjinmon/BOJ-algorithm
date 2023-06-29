# 2309 일곱 난쟁이
temp = []
for _ in range(9):
    temp.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        if sum(temp)-temp[i]-temp[j] == 100:
            delete1 = temp[i]
            delete2 = temp[j]
temp.remove(delete1)
temp.remove(delete2)
for i in sorted(temp):
    print(i)