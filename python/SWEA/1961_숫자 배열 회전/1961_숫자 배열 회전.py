import sys

sys.stdin = open('input.txt')

T = int(input())

# 90도 회전
def nt_degree(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    i = len(matrix) - 1
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            new_matrix[c][i] = matrix[r][c]                         # 90도 회전일 때는 이전의 열번호가 행번호로 변하고 열은 최대 인덱스에서 1씩 작아짐
        i -= 1
    return new_matrix

# 180도 회전
def oet_detree(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    i = len(matrix) - 1
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            new_matrix[i][c] = matrix[r][len(matrix) - c - 1]       # 180도 회전일 때는 행이 최대 인덱스에서 1씩 작아지며 열은 최대 인덱스에서 1을 뺀 값과 같아짐 
        i -= 1

    return new_matrix

# 270도 회전
def tst_degree(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    i = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            new_matrix[len(metrix) - 1 - c][i] = matrix[r][c]       # 270도 회전일 때는 180도 회전일 때와 행과 열만 서로 달라짐
        i += 1

    return new_matrix

for tc in range(1, T + 1):
    N = int(input())
    metrix = [list(input().split()) for _ in range(N)]

    nt = nt_degree(metrix)
    oet = oet_detree(metrix)
    tst = tst_degree(metrix)

    print(f'#{tc}')
    for row in range(N):
        print(f'{"".join([str(x) for x in nt[row]])} {"".join([str(x) for x in oet[row]])} {"".join([str(x) for x in tst[row]])}')

