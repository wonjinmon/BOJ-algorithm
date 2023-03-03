# 1259 팰린드롬수
while True:
    a = input()
    if a =='0':
        break
    a=list(a)
    if a == a[::-1]:
        print('yes')
    else:
        print('no')
        