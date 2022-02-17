import sys

sys.stdin = open('input.txt')

T = int(input())

# 가로 검증 함수
def widthIns(lst):
    for num in range(1, 10):
        if num not in lst:
            return 1
    return 0

# 격자 검증 함수
# 격자를 조회할 때는 인덱스에 주의해야 함
# 스도쿠는 3*3 간격으로 되어 있으니 이를 고려해줘야 함
def gridIns(matrix):
    for r in range(0, len(matrix) - 3 + 1, 3):
        for c in range(0, len(matrix[r]) - 3 + 1, 3):
            sum_num = 0
            for i in range(3):
                for j in range(3):
                    sum_num += matrix[r+i][c+j]

            if sum_num != 45:
                return 1
    return 0



for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_cross = list(zip(*sudoku)) # 전치행렬
    is_sudoku_ok = 0

    # 가로검증
    for row in range(len(sudoku)):
        is_sudoku_ok += widthIns(sudoku[row])
        if is_sudoku_ok > 0:
            break
    
    # 전치행렬을 이용한 세로검증
    for col in range(len(sudoku_cross)):
        is_sudoku_ok += widthIns(sudoku_cross[col])
        if is_sudoku_ok > 0:
            break

    # 격자검증
    is_sudoku_ok += gridIns(sudoku)

    if is_sudoku_ok > 0:
        is_sudoku_ok = 0
    else:
        is_sudoku_ok = 1

    print(f'#{tc} {is_sudoku_ok}')

