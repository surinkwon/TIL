'''
bfs

파이썬으로 하면 시간초과, 파이파이는 통과
나중에 파이썬으로 시간초과 안 나게도 해보자
보물이 있는 최솟값을 찾으라고 했지만 결국에는 최대로 멀리 떨어져 있는 곳을 가는 시간을 구하면 됨
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def findWay(r, c):
    q = deque()
    v = [[0] * M for _ in range(N)]
    v[r][c] = 1
    q.append((r, c))
    tmp = 0

    while q:
        cr, cc = q.popleft()
        tmp = v[cr][cc]

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and treasure_map[nr][nc] == 'L' and v[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1

    return tmp - 1


N, M = map(int, input().split())
treasure_map = [list(input()) for _ in range(N)]
min_d = 0

for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            rlt = findWay(i, j)
            min_d = max(min_d, rlt)

print(min_d)