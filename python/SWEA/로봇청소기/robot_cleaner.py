import sys

sys.stdin = open('input.txt')

T = 1

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
for tc in range(1, T + 1):
    total = 0
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    nr = r
    nc = c

    while True:
        if room[nr][nc] == 0:
            r = nr
            c = nc
            room[r][c] = 2
            total += 1

        if room[r][c + 1] and room[r][c - 1] and room[r + 1][c] and room[r - 1][c]:
            if room[r+dr[(d + 2) % 4]][c+dc[(d + 2) % 4]] == 1:
                break
            elif room[r+dr[(d + 2) % 4]][c+dc[(d + 2) % 4]] == 2:
                r += dr[(d+2) % 4]
                c += dc[(d + 2) % 4]
                continue

        d = (d + 1) % 4

        nr = r + dr[d]
        nc = c + dc[d]

    print(total)


