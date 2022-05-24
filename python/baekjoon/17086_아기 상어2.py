'''
bfs
'''
from collections import deque

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def howFar(r, c):
    q = deque()
    v = [[0] * M for _ in range(N)]
    v[r][c] = 1
    q.append((r, c))

    while q:
        cr, cc = q.popleft()

        if room[cr][cc]:
            return v[cr][cc] - 1
        
        for d in range(8):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
max_sd = 0

for i in range(N):
    for j in range(M):
        if room[i][j] == 0:
            sd = howFar(i, j)
            max_sd = max(max_sd, sd)

print(max_sd)