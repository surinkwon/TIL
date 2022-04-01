'''
벽이 없는 곳의 좌표를 받고 3개씩 고를 수 있는 모든 경우를 구함
번갈아가면서 벽을 세우고 bfs
'''
from itertools import combinations
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def spread(start, cnt):
    v = [[0] * M for _ in range(N)]
    q = deque()
    for i in range(len(start)):
        v[start[i][0]][start[i][1]] = 1
        q.append((start[i][0], start[i][1]))
    
    while q:
        cr, cc = q.popleft()

        # 가지치기
        if cnt <= max_safty_place:
            return 0
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0 and lab[nr][nc] == 0:
                v[nr][nc] = 1
                q.append((nr, nc))
                cnt -= 1
        
    return cnt


# 연구소 데이터 입력
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스, 벽 없는 곳 좌표 저장
virus = []
no_walls = []
safty_place = 0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            no_walls.append((i, j))
            safty_place += 1

safty_place -= 3
max_safty_place = 0

# 벽이 없는 곳 중 세 개를 선택(모든 경우)
per = list(combinations(no_walls, 3))

# 모든 경우를 돌며 벽을 세우고 바이러스가 얼마나 퍼지는지 확인
for i in range(len(per)):
    lab[per[i][0][0]][per[i][0][1]] = lab[per[i][1][0]][per[i][1][1]] = lab[per[i][2][0]][per[i][2][1]] = 1
    tmp = spread(virus, safty_place)

    if max_safty_place < tmp:
        max_safty_place = tmp
        
    lab[per[i][0][0]][per[i][0][1]] = lab[per[i][1][0]][per[i][1][1]] = lab[per[i][2][0]][per[i][2][1]] = 0
    
print(max_safty_place)

