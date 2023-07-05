from collections import deque

# 얼마나 많은 마을의 배달을 받을 수 있는지 구하는 함수
def howManyTown(s, road_lst, distance, K):
    q = deque()
    v = [0] * len(road_lst)
    q.append((1, 0))
    town_num = 1
    
    while q:
        ct, cd = q.popleft()
        
        for d in range(len(road_lst[ct])):
            nt = road_lst[ct][d]

            if nt > 1 and cd + distance[ct][nt] <= K:

                if v[nt] and v[nt] > cd + distance[ct][nt]:
                    q.append((nt, cd + distance[ct][nt]))
                    v[nt] = cd + distance[ct][nt]

                elif v[nt] == 0:
                    q.append((nt, cd + distance[ct][nt]))
                    v[nt] = cd + distance[ct][nt]
                    town_num += 1
    return town_num

def solution(N, road, K):
    answer = 0
    
    road_lst = [[] for _ in range(N + 1)]
    distance = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 도로 정보 저장
    for i in range(len(road)):
        a, b, d = road[i]

        if distance[a][b]:
            distance[a][b] = min(distance[a][b], d)
            distance[b][a] = min(distance[b][a], d)

        else:
            road_lst[a].append(b)
            road_lst[b].append(a)
            distance[a][b] = d
            distance[b][a] = d
    
    answer = howManyTown(1, road_lst, distance, K)
    
    return answer