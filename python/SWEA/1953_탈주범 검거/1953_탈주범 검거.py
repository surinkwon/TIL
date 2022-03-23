import sys

sys.stdin = open('input.txt')

T = int(input())

# 각 구조물 별 방향과 해당 방향과 연결된 구조물의 숫자
dr = [[0], [0, 1, 0, -1], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
dc = [[0], [1, 0, -1, 0], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]
connect = [[0],
           [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]],
           [[1, 2, 5, 6], [1, 2, 4, 7]],
           [[1, 3, 4, 5], [1, 3, 6, 7]],
           [[1, 2, 5, 6], [1, 3, 6, 7]],
           [[1, 2, 4, 7], [1, 3, 6, 7]],
           [[1, 2, 4, 7], [1, 3, 4, 5]],
           [[1, 2, 5, 6], [1, 3, 4, 5]]]


def whereTheif(base, r, c, t):
    v = [[0] * len(base[0]) for _ in range(len(base))]
    v[r][c] = 1
    queue = [0] * (len(base[0]) * len(base))
    qr = 0
    queue[qr] = (r, c)
    qf = -1

    theif = 1 # 도둑이 있을 수 있는 공간 수

    while qf != qr:
        qf += 1
        r, c = queue[qf][0], queue[qf][1]

        if v[r][c] == t: # 시간이 다 지났으면 그만 둚
            break

        struture = base[r][c]

        for d in range(len(dr[struture])):
            nr = r + dr[struture][d]
            nc = c + dc[struture][d]

            if 0 <= nr < len(base) and 0 <= nc < len(base[0]):
                # 해당 공간에 방문했는지뿐만 아니라 해당 공간의 구조물과 지금 구조물이 연결되어 있는지도 검사
                if base[nr][nc] in connect[struture][d] and not v[nr][nc]:
                    v[nr][nc] = v[r][c] + 1
                    qr += 1
                    queue[qr] = (nr, nc)
                    theif += 1
                    
    # 시간이 다 지나기 전에 길이 막혀서 도둑이 더 이상 가지 못 할 수도 있기 때문에
    # 가장 아래에서 반환해줌
    return theif


for tc in range(1, T + 1):
    N, M, sr, sc, time = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]

    rlt = whereTheif(B, sr, sc, time)

    print(f'#{tc} {rlt}')
