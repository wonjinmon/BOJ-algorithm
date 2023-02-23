# 10808 알파벳 개수
word = list(input())

abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(abc)):
    print(word.count(abc[i]), end = ' ')