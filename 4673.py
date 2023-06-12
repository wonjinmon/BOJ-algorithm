# 4673 셀프 넘버

def self_number(n):
    b = int(n)
    for i in range(len(str(n))):
        b += int(str(n)[i]) 
    return b

result = []
for i in range(1,10001):
    result.append(self_number(i))
    if i not in result:
        print(i)