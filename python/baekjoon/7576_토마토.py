'''
토마토 정보를 받을 때 익지 않은 토마토 개수와 익은 토마토 개수를 받음
bfs를 이용해 토마토 익은 것을 확인
다 돌았는데도 익은 게 남았으면 -1 출력
'''

from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(rtomato, urt):
    v = [[0] * M for _ in range(N)]
    q = deque()
    for i in range(len(rtomato)):
        v[rtomato[i][0]][rtomato[i][1]] = 1
        q.append((rtomato[i][0], rtomato[i][1]))
    
    while q:
        cr, cc = q.popleft()

        if urt == 0:
            if q:
                r, c = q.pop()
                return v[r][c] - 1
            else:
                return v[cr][cc] - 1
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 and v[nr][nc] == 0:
                v[nr][nc] = v[cr][cc] + 1
                q.append((nr, nc))
                urt -= 1
    
    return -1



M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

ripe = []
unripe = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe.append((i, j))
        elif box[i][j] == 0:
            unripe += 1

min_days = bfs(ripe, unripe)

print(min_days)