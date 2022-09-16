'''
BFS
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 목표지점부터 거리 구하는 함수
def calDistances(sr, sc):
    q = deque()
    v = [[0] * M for _ in range(N)]
    v[sr][sc] = 1
    q.append((sr, sc))

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and jido[nr][nc] and v[nr][nc] == 0:
                v[nr][nc] = v[cr][cc] + 1
                q.append((nr, nc))
    
    # 원래 갈 수 있는 곳(지도상 1인 곳)인데 못 가는 경우 계산
    for r in range(N):
        for c in range(M):
            if v[r][c] == 0 and jido[r][c] == 0:
                continue
            else:
                v[r][c] -= 1
                
    
    return v


N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if jido[r][c] == 2:
            gr, gc = r, c
            break

distances = calDistances(gr, gc)

for i in range(N):
    for j in range(M):
        print(distances[i][j], end=' ')
    print()