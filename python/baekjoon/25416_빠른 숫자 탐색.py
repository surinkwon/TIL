'''
bfs로 풀이
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def findWay(sr, sc):
    q = deque()
    q.append((sr, sc))
    v = [[0] * 5 for _ in range(5)]
    v[sr][sc] = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < 5 and 0 <= nc < 5 and not v[nr][nc] and matrix[nr][nc] != -1:
                if matrix[nr][nc] == 0:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc] + 1
                else:
                    return v[cr][cc]

    return -1


matrix = [list(map(int, input().split())) for _ in range(5)]
sr, sc = map(int, input().split())

rlt = findWay(sr, sc)

print(rlt)