'''
다익스트라
'''
import sys
from collections import deque

# 최소 거리 찾는 함수, 한 지점에서 시작하면 그 지점에서 다른 지점으로 가는 최소경로를 모두 구할 수 있음
def findWay(start):
    q = deque()
    v = [9999999] * (n + 1)
    q.append(start)
    v[start] = 0

    while q:
        cn = q.popleft()

        for d in range(len(road[cn])):
            if v[road[cn][d]] > v[cn] + road_d[cn][road[cn][d]]:
                v[road[cn][d]] = v[cn] + road_d[cn][road[cn][d]]
                q.append(road[cn][d])
    
    # 갈 수 없을 경우도 고려해야 함
    for i in range(len(v)):
        if v[i] == 9999999:
            v[i] = 0
    return v
    


n = int(input())
m = int(input())
road = [[] for _ in range(n + 1)]
road_d = [[9999999] * (n + 1) for _ in range(n + 1)]
rlt = []

for _ in range(m):
    s, e, d = map(int, sys.stdin.readline().split())
    # 같은 경로로 가능 길이 여러 개 주어질 수도 있기 때문에 처리해줌
    if e not in road[s]:
        road[s].append(e)
    road_d[s][e] = min(road_d[s][e], d)

for i in range(1, n + 1):
    rlt.append(findWay(i))

for i in range(n):
    print(' '.join([str(rlt[i][x]) for x in range(1, len(rlt[0]))]))

