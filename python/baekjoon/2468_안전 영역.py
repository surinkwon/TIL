'''
비가 1~100까지 오는 경우를 보며 물에 잠기는 곳을 제외한 영역을 돌며 개수 체크
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check(r, c):
    global v
    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and region[nr][nc] > rain:
                q.append((nr, nc))
                v[nr][nc] = 1


N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]
max_safty = 0

# 높이가 다 1인 경우가 있을 수 있기 때문에 비가 아예 내리지 않는 경우도 고려
for rain in range(101):
    v = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and region[i][j] > rain:
                cnt += 1
                check(i, j)
    
    max_safty = max(max_safty, cnt)

print(max_safty)


