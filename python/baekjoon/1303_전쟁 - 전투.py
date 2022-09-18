from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 병사 수 세고 힘 반환하는 함수
def calPower(sr, sc, who):
    global v
    q = deque()
    v[sr][sc] = 1
    q.append((sr, sc))
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < M and 0 <= nc < N and v[nr][nc] == 0 and battle_field[nr][nc] == who:
                q.append((nr, nc))
                v[nr][nc] = 1
                cnt += 1
    
    return cnt ** 2

N, M = map(int, input().split())

battle_field = [list(input()) for _ in range(M)]
v = [[0] * N for _ in range(M)]

me = enemy = 0

for i in range(M):
    for j in range(N):
        if v[i][j] == 0:
            if battle_field[i][j] == 'W':
                me += calPower(i, j, 'W')
            else:
                enemy += calPower(i, j, 'B')

print(me, enemy)


