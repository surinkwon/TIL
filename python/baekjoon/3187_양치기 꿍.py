'''
bfs
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def whatHappen(r, c, n):
    global land
    q = deque()
    v = [[0] * M for _ in range(N)]
    q.append((r, c))
    v[r][c] = 1

    sheep = 0
    wolves = 0
    if n == 'v':
        wolves += 1
    else:
        sheep += 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and land[nr][nc] != '#' and v[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = 1
                if land[nr][nc] == 'v':
                    wolves += 1
                elif land[nr][nc] == 'k':
                    sheep += 1
                land[nr][nc] = '#'
    
    if wolves >= sheep:
        return 0, wolves
    else:
        return sheep, 0



N, M = map(int, input().split())

land = [list(input()) for _ in range(N)]
alive_sheep = 0
alive_wolves = 0

for i in range(N):
    for j in range(M):
        if land[i][j] == 'v' or land[i][j] == 'k':
            sheep, wolves = whatHappen(i, j, land[i][j])
            alive_sheep += sheep
            alive_wolves += wolves

print(alive_sheep, alive_wolves)
