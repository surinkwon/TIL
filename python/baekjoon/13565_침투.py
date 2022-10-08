'''
bfs로 풀이
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def checkElectric(r, c):
    global v

    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()

        # 전류가 통하면 1반환
        if cr == R - 1:
            return 1

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < R and 0 <= nc < C and not v[nr][nc] and not matrix[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = 1

    return 0


R, C = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(R)]

v = [[0] * C for _ in range(R)]
can = 'NO'

for i in range(C):
    # 바깥쪽이 전류가 통할 수 있는 부분이면 검사
    if not matrix[0][i] and not v[0][i]:
        rlt = checkElectric(0, i)

        if rlt:
            can = 'YES'
            break

print(can)