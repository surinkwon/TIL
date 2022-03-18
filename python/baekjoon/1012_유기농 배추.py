from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    q = deque()
    q.append((r, c))
    field[r][c] = 0

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + dr[d], cj + dc[d]
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj]:
                field[ni][nj] = 0
                q.append((ni, nj))


T = int(input())

for _ in range(T):
    M, N, cabbage = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    worm = 0

    for _ in range(cabbage):
        c, r = map(int, input().split())
        field[r][c] = 1
    
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                # BFS로 밭에 배추가 있는 곳만 없다고 표시해줌
                BFS(i, j)
                worm += 1

    print(worm)
