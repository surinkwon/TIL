'''
bfs
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def contagion():
    global case
    v = [[0] * N for _ in range(N)]
    q = deque()
    # 1번 바이러스부터 퍼지므로 1번부터 모두 넣어줌
    for i in range(1, len(virus_loc)):
        for j in range(len(virus_loc[i])):
            q.append(virus_loc[i][j])
            v[virus_loc[i][j][0]][virus_loc[i][j][1]] = 1
    
    while q:
        cr, cc = q.popleft()

        # 해당 칸을 방문했을 때의 시간이 조건과 같으면 그만 퍼뜨림
        # 원래는 S지만 처음 칸을 1이라고 했으므로 S+1일 때로 지정
        if v[cr][cc] == S + 1:
            return
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0:
                v[nr][nc] = v[cr][cc] + 1
                case[nr][nc] = case[cr][cc]
                q.append((nr, nc))


N, K = map(int, input().split())
case = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 바이러스 위치 담기
virus_loc = [[] for _ in range(K + 1)]
for i in range(N):
    for j in range(N):
        if case[i][j]:
            virus_loc[case[i][j]].append((i, j))

# 전염
contagion()

rlt = case[X-1][Y-1]

print(rlt)
