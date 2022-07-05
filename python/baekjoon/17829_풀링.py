import sys

# 두 번째로 큰 수를 찾는 함수
def findSecond(r, c):
    nums = []
    for i in range(2):
        for j in range(2):
            nums.append(board[r+i][c+j])
    
    nums.sort()
    return nums[-2]

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
new_board = [[0] * (N // 2) for _ in range(N // 2)]

while True:
    for r in range(0, len(board), 2):
        for c in range(0, len(board), 2):
            second_big_num = findSecond(r, c)
            new_board[r // 2][c // 2] = second_big_num
    
    if len(new_board) == 1:
        print(new_board[0][0])
        break

    board = new_board
    new_board = [[0] * (len(board) // 2) for _ in range(len(board) // 2)]


