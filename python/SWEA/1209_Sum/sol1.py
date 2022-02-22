import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    # 가로 덧셈
    for r in range(len(matrix)):
        ssum = 0
        for c in range(len(matrix[r])):
            ssum += matrix[r][c]

        if max_sum < ssum:
            max_sum = ssum

    # 세로 덧셈
    for c in range(len(matrix[0])):
        ssum = 0
        for r in range(len(matrix)):
            ssum += matrix[r][c]

        if max_sum < ssum:
            max_sum = ssum

    # 대각선 덧셈
    dsum = 0
    drsum = 0
    for rc in range(len(matrix)):
        dsum += matrix[rc][rc]
        drsum += matrix[rc][len(matrix[rc]) - 1 - rc]

    if max_sum < dsum:
        max_sum = dsum

    if max_sum < drsum:
        max_sum = drsum

    print(f'#{tc} {max_sum}')

