'''
치킨집 좌표를 받고 지도에서는 지움(안 지워도 됨 그냥 좌표로 풀면 됨)
집 좌표를 받음
치킨 집 좌표 중 M 개를 선택(M개를 선택하는 모든 경우를 구함)
모든 경우에 대해 각 집과 치킨집의 최소 거리를 구하고 더해서 총 최소 거리에 저장
더 작은 최소 거리가 나오면 갱신
'''

from itertools import combinations


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
houses = []

# 치킨집, 집 좌표 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))

# 치킨 집 중 M개를 고르는 모든 경우를 구함
choose = list(combinations(chicken, M))
# 가장 작은 최종 거리
min_total_d = 9876543

# M개를 고른 모든 경우를 돌면서 검사
for i in range(len(choose)):
    # 여기에서 초기화 해줘야 매 경우마다 정확히 계산 가능
    # 앞에서 초기화 한 번만 해주면 지금 경우에선 나올 수 없는 최솟값이 계속 저장되어 있어서
    # 제대로 값을 구할 수 없음
    min_d = [9876543] * len(houses)

    # 모든 집 좌표를 돌면서
    for house_id in range(len(houses)):
        
        # 각 집에 대해 다시 모든 치킨집과의 거리를 구하고 가장 작은 거리만 저장
        for ch in range(len(choose[i])):
            # 치킨집의 좌표
            ch_r = choose[i][ch][0]
            ch_c = choose[i][ch][1]
            
            # 집의 좌표
            house_r = houses[house_id][0]
            house_c = houses[house_id][1]
            d = abs(ch_r-house_r) + abs(ch_c-house_c)

            # 거리가 더 작을 때만 저장
            if min_d[house_id] > d:
                min_d[house_id] = d
    
    # 모든 집 좌표에 대해 다 돌았으면 최종 거리 구하고 
    # 현재 최종 거리가 이전보다 작을 때만 갱신
    total = sum(min_d)
    if min_total_d > total:
        min_total_d = total

print(min_total_d)

