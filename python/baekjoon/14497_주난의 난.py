'''
다익스트라
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def jump(r, c):
    q = deque()
    v = [[9999999] * M for _ in range(N)]
    q.append((r, c))
    v[r][c] = 0

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if class_room[cr][cc] != '0' and v[nr][nc] > v[cr][cc] + 1:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc] + 1
                elif class_room[cr][cc] == '0' and v[nr][nc] > v[cr][cc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[cr][cc]

    return v[gr][gc]


N, M = map(int, input().split())
jr, jc, gr, gc = map(lambda x: int(x) - 1, input().split())

class_room = [list(input()) for _ in range(N)]

min_cnt = jump(jr, jc)

print(min_cnt)
