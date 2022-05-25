'''
bfs
다익스트라
'''
from collections import deque
import sys

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def findWay(sr, sc):
    q = deque()
    q.append((sr, sc))
    v = [[999999] * M for _ in range(N)]
    v[sr][sc] = 0

    while q:
        cr, cc= q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] and v[nr][nc] > v[cr][cc] + 1:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc] + 1
                elif maze[nr][nc] == 0 and v[nr][nc] > v[cr][cc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc]
    
    return v[N-1][M-1]


M, N = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

rlt = findWay(0, 0)

print(rlt)

