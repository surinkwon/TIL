'''
bfs
'''
from collections import deque

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def findLetter(r, c):
    global v
    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()

        for d in range(8):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and banner[nr][nc] and not v[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = 1
    
    return 1

N, M = map(int , input().split())

banner = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
letter_num = 0

for i in range(N):
    for j in range(M):
        if banner[i][j] and not v[i][j]:
            letter_num += findLetter(i, j)

print(letter_num)