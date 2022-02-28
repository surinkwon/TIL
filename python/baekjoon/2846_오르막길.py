N = int(input())
road = list(map(int, input().split()))
up = []

dis = 0
for i in range(1, len(road) + 1):
    if i < len(road) and road[i] > road[i - 1]: # 마지막 인덱스까지 포함시키기 위한 조건 설정
        dis += 1
    else:
        up.append(road[i - 1] - road[i - 1 - dis])
        dis = 0

if up:
    print(max(up))
else:
    print(0)
