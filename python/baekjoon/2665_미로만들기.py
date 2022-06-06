'''
다익스트라
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def findWay():
    q = deque()
    v = [[999999] * N for _ in range(N)]
    q.append((0, 0))
    v[0][0] = 0

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 0 and v[nr][nc] > v[cr][cc] + 1:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc] + 1
                if maze[nr][nc] and v[nr][nc] > v[cr][cc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc]
    
    return v[N-1][N-1]



N = int(input())
maze = [list(map(int, input())) for _ in range(N)]

rlt = findWay()

print(rlt)
