'''
bfs, 3차원 배열
'''
from collections import deque
import sys

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, -1, 0, 1, 0, 0]
df = [0, 0, 0, 0, 1, -1]

def findWay(s):
    q = deque()
    q.append(s)
    v = [[[0] * C for _ in range(R)] for _ in range(L)]
    v[s[0]][s[1]][s[2]] = 1

    while q:
        cf, cr, cc = q.popleft()

        if (cf, cr, cc) == end:
            return f'Escaped in {v[cf][cr][cc] - 1} minute(s).' 
        
        for d in range(6):
            nf, nr, nc = cf + df[d], cr + dr[d], cc + dc[d]

            if 0 <= nf < L and 0 <= nr < R and 0 <= nc < C:
                if v[nf][nr][nc] == 0 and building[nf][nr][nc] != '#':
                    q.append((nf, nr, nc))
                    v[nf][nr][nc] = v[cf][cr][cc] + 1
        
    return 'Trapped!'


while True:
    L, R, C = map(int, input().split())

    if L or R or C:
        start = 0
        end = 0
        building = [[] for _ in range(L)]
        
        # 빌딩 정보 받기

        for i in range(L):
            building[i] = [list(sys.stdin.readline().strip()) for _ in range(R)]
            if start == 0:
                for r in range(R):
                    for c in range(C):
                        if building[i][r][c] == 'S':
                            start = (i, r, c)
            
            if end == 0:
                for r in range(R):
                    for c in range(C):
                        if building[i][r][c] == 'E':
                            end = (i, r, c)

            space = input()
        
        rlt = findWay(start)

        print(rlt)
    else:
        break