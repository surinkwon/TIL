'''
서로 다른 조건으로 bfs 돌리면 됨
주의
- 적록색약 -> 빨강과 초록 구분 X -> 빨강과 초록이 같다는 조건만 넣어주면 안 됨, 초록이 빨강과 같다는 조건도 넣어줘야함
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def devide(color, r, c, cb):
    global v1, v2
    q = deque()
    # 색약이 있는지 없는지에 따라 방문 배열을 설정
    if cb:
        v = v2
    else:
        v = v1
    v[r][c] = 1
    q.append((r, c))

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                # 색약이 있으면, 방문하지 않았으면, 이전 컬러와 같거나 이전 컬러가 빨강, 초록인데 현재는 초록, 빨강이면
                if cb and v[nr][nc] == 0 and (picture[nr][nc] == color or (color == 'R' and picture[nr][nc] == 'G' or color == 'G' and picture[nr][nc] == 'R')):
                    v[nr][nc] = 1
                    q.append((nr, nc))
                elif cb == 0 and v[nr][nc] == 0 and picture[nr][nc] == color:
                    v[nr][nc] = 1
                    q.append((nr, nc))


N = int(input())
picture = [list(input()) for _ in range(N)]
v1 = [[0] * N for _ in range(N)]
v2 = [[0] * N for _ in range(N)]
cnt1 = cnt2 = 0

for i in range(N):
    for j in range(N):
        if v1[i][j] == 0:
            cnt1 += 1
            devide(picture[i][j], i, j, 0)
        if v2[i][j] == 0:
            cnt2 += 1
            devide(picture[i][j], i, j, 1)            

print(cnt1, cnt2)