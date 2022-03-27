import sys

sys.stdin = open('input.txt')

T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
st = [0, [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
opp = [2, 3, 0, 1]


def BFS(i, j):
    q = []
    v = [[0] * M for _ in range(N)]
    q.append((i, j))
    v[i][j] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if v[ci][cj] == L:
            return cnt

        for d in range(4):
            if st[base[ci][cj]][d]:
                ni, nj = ci + dr[d], cj + dc[d]
                if 0 <= ni < N and 0 <= nj < M and base[ni][nj] and v[ni][nj] == 0 and st[base[ni][nj]][opp[d]]:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
                    cnt += 1

    return cnt



for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]
    rlt = BFS(R, C)

    print(f'#{tc} {rlt}')