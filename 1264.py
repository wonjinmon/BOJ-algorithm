# 1264 모음의 개수

m = [ 'a', 'e', 'i', 'o', 'u']

while True:
    sentence = str(input()).lower()
    if sentence == '#':
        break
    cnt = 0
    for i in m:
        cnt += sentence.count(i)
    print(cnt)