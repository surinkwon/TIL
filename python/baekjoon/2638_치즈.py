'''
bfs

바깥 쪽의 빈 공간과 치즈를 방문처리하고
안 쪽의 빈 공간은 방문처리 하지 않으면 빈 공간이 외부인지 내부인지를 알 수 있게 됨
이를 이용해서 외부 공기와 접촉한 곳만 녹임
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def melt():
    global plate
    plate_q = deque()
    cheese = []
    v = [[0] * M for _ in range(N)]
    plate_q.append((0, 0))
    v[0][0] = 1
    melted = 0

    # 겉면에 있는 치즈를 구별
    while plate_q:
        cr, cc = plate_q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:

                # 이전에 방문한 적 없는 곳이 치즈라면 치즈 리스트에 추가, 방문처리
                if plate[nr][nc]:
                    cheese.append((nr, nc))
                    v[nr][nc] = 1
                
                # 빈 곳이면 큐에 추가, 방문처리
                else:
                    plate_q.append((nr, nc))
                    v[nr][nc] = 1
    
    # 겉에 있는 치즈 녹이기
    for i in range(len(cheese)):
        cnt = 0
        cr, cc = cheese[i]

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if plate[nr][nc] == 0 and v[nr][nc]:
                cnt += 1
        
        if cnt > 1:
            plate[cr][cc] = 0
            v[cr][cc] = 0
            melted += 1
    
    return melted


N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

time = 0
# 치즈가 다 녹을 때까지 시간을 잼
while True:
    rlt = melt()
    if rlt == 0:
        print(time)
        break

    time += 1