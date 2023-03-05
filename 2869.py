a,b,v = map(int, input().split())

if (v-b) % (a-b) == 0:
    print(int((v-b) / (a-b)))
else:
    print(int((v-b) / (a-b) + 1))

# while문 사용시 시간초과
# 하루에 올라가는 거리 a-b, 정상에 도착하면 미끄러짐 X 따라서 정상은 v-b
# (v-b) % (a-b) 값이 나누어 떨어지면 바로 정상, 그게 아니라면 하루 더 필요