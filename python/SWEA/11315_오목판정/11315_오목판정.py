import sys

sys.stdin = open('input.txt')

T = int(input())


def width(matrix):
    for r in range(len(matrix)):
        cnt = 0
        for c in range(len(matrix)):
           if matrix[r][c] == 'o':
               cnt += 1
               if cnt == 5:
                   return 1
           else:
               cnt = 0
    return 0


def vertical(matrix):
    for c in range(len(matrix)):
        cnt = 0
        for r in range(len(matrix)):
            if matrix[r][c] == 'o':
                cnt += 1
                if cnt == 5:
                    return 1
            else:
                cnt = 0
    return 0


def dia(matrix):
    for r in range(len(matrix) - 4):
        for c in range(len(matrix) - 4):
            cnt = 0
            for i in range(5):
                if matrix[r+i][c+i] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 1
                else:
                    cnt = 0
    return 0


def dia_r(matrix):
    for r in range(len(matrix) - 4):
        for c in range(len(matrix) - 1, 3, -1):
            cnt = 0
            for i in range(5):
                if matrix[r+i][c-i] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 1
                else:
                    cnt = 0
    return 0


for tc in range(1, T + 1):
    N = int(input())
    checkerboard = [list(input()) for _ in range(N)]
    rlt = 0

    rlt += width(checkerboard)
    rlt += vertical(checkerboard)
    rlt += dia(checkerboard)
    rlt += dia_r(checkerboard)

    if rlt:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

