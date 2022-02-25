import sys

sys.stdin = open('input.txt')

T = int(input())


# 수익 계산 함수
def profit(matrix, num):
    p = 0
    for r in range(len(matrix)):
        if r <= num // 2:
            c = num // 2 - r
            for i in range(2 * r + 1):
                p += matrix[r][c + i]
        else:
            nr = num - (r + 1)
            c = num // 2 - nr
            for i in range(2 * nr + 1):
                p += matrix[r][c + i]

    return p


for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    rlt = profit(farm, N)
    print(f'#{tc} {rlt}')

