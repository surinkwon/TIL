'''
bfs
'''
from collections import deque
import sys

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def howBig(r, c):
    global corridor

    q = deque()
    v = [[0] * (M + 1) for _ in range(N + 1)]
    v[r][c] = 1
    q.append((r, c))
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 < nr < N + 1 and 0 < nc < M + 1 and corridor[nr][nc] and not v[nr][nc]:
                q.append((nr, nc))
                cnt += 1
                v[nr][nc] = 1
                corridor[nr][nc] = 0
    
    return cnt


N, M, K = map(int, input().split())
corridor = [[0] * (M + 1) for _ in range(N + 1)]
max_ammount = 0

for _ in range(K):
    data = list(map(int, sys.stdin.readline().split()))
    corridor[data[0]][data[1]] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if corridor[i][j]:
            corridor[i][j] = 0
            tmp = howBig(i, j)
            max_ammount = max(max_ammount, tmp)

print(max_ammount)
