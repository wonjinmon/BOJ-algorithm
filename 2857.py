# 2857 FBI
temp = []

for i in range(1,6):
    name = input()
    if name.count('FBI') >=1:
        temp.append(i)
if len(temp) > 0:  
    for i in range(len(temp)):
        print(temp[i], end=' ')
else:
    print('HE GOT AWAY!')