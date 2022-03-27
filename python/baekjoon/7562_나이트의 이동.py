from collections import deque

# 나이트가 이동할 수 있는 칸
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

def findWay(i, j, goal_i, goal_j):
    v = [[0] * N for _ in range(N)]
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()

        if ci == goal_i and cj == goal_j:
            return v[ci][cj] - 1
        
        for d in range(8):
            ni, nj = ci + dr[d], cj + dc[d]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1



T = int(input())

for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    gi, gj = map(int, input().split())

    rlt = findWay(si, sj, gi, gj)

    print(rlt)