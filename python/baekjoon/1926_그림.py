'''
BFS
스케치북에 그려진 그림의 개수와 가장 넓은 그림의 크기를 찾는 문제
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def findPainting(sr, sc):
    global v
    q = deque()
    v[sr][sc] = 1
    q.append((sr, sc))
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0 and sketchbook[nr][nc]:
                q.append((nr, nc))
                cnt += 1
                v[nr][nc] = 1
    
    return cnt


N, M = map(int, input().split())

sketchbook = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
paint_num = 0
max_width = 0

for i in range(N):
    for j in range(M):
        if sketchbook[i][j] and not v[i][j]:
            tmp_width =  findPainting(i, j)
            max_width = max(max_width, tmp_width)
            paint_num += 1

print(paint_num)
print(max_width)