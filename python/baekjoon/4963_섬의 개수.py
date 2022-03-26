'''
방문 배열을 두고 섬이 있으면서 방문하지 않았다면 BFS돌려서 섬 너비만큼 방문 체크
'''
from collections import deque

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def checkIsland(r, c):
    global v
    q = deque()
    q.append([r, c])
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()

        for d in range(8):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < len(v) and 0 <= nc < len(v[0]) and v[nr][nc] == 0 and ocean[nr][nc]:
                q.append([nr, nc])
                v[nr][nc] = 1
    
    return


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        ocean = [list(map(int, input().split())) for _ in range(h)]
        v = [[0] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if ocean[i][j] and v[i][j] == 0:
                    checkIsland(i, j)
                    cnt += 1
        
        print(cnt)