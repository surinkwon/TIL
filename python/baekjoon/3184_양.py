'''
bfs
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def whatHappen(r, c):
    global v
    q = deque()
    v[r][c] = 1
    q.append((r, c))
    sheep_num = 0
    wolves_num = 0
    if yard[r][c] == 'v':
        wolves_num += 1
    elif yard[r][c] == 'o':
        sheep_num += 1
    
    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < R and 0 <= nc < C and v[nr][nc] == 0 and yard[nr][nc] != '#':
                if yard[nr][nc] == 'v':
                    wolves_num += 1
                elif yard[nr][nc] == 'o':
                    sheep_num += 1
                q.append((nr, nc))
                v[nr][nc] = 1

    if sheep_num > wolves_num:
        return sheep_num, 0
    else:
        return 0, wolves_num

R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]
v = [[0] * C for _ in range(R)]
alive_sheep = 0
alive_wolves = 0

for i in range(R):
    for j in range(C):
        if yard[i][j] != '#' and v[i][j] == 0:
            sheep, wolves = whatHappen(i, j)
            alive_sheep += sheep
            alive_wolves += wolves

print(alive_sheep, alive_wolves)