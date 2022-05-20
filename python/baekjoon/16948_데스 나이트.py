'''
bfs
'''
from collections import deque

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

def move():
    q = deque()
    q.append((r1, c1))
    v = [[0] * N for _ in range(N)]
    v[r1][c1] = 1

    while q:
        cr, cc = q.popleft()

        if cr == r2 and cc == c2:
            return v[cr][cc] - 1
        
        for d in range(6):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1

    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

min_move = move()

print(min_move)