'''
사각형 영역을 표시하고 bfs로 영역 넓이 체크
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check(r, c):
    global paper
    q = deque()
    q.append((r, c))
    paper[r][c] = 1
    size = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < M and 0 <= nc < N and paper[nr][nc] == 0:
                q.append((nr, nc))
                paper[nr][nc] = 1
                size += 1

    return size



M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]
width = []
cnt = 0

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    ly = -(ly - (M - 1))
    ry = -(ry - (M - 1))

    for i in range(ry + 1, ly + 1):
        for j in range(lx, rx):
            paper[i][j] = 1

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            cnt += 1
            s = check(i, j)
            width.append(s)

print(cnt)
print(' '.join([str(x) for x in sorted(width)]))