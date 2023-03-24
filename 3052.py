# 3052 나머지
val = []
for _ in range(10):
    a = int(input())
    val.append(a % 42)

result = []
count = 0
for i in val:
    if i not in result:
        result.append(i)
        count += 1
print(count)