# 체스판을 완전 탐색해서 최솟값 갱신
# 가능한 체스판은 두 가지이므로 미리 만들어놓고 비교
'''
체스판 하나만 만들어놓고 해도 됨...
하나의 체스판은 다른 체스판의 정 반대이기 때문에 하나의 체스판에서 맞지 않는 개수를 구했으면
다른 체스판에서는 자동으로 체스판 크기에서 그 개수를 뺀 것이 됨
'''
chess_board1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

chess_board2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# 다시 칠해야하는 사각형 개수 구하는 함수
def recoloring(b, r, c):
    cnt1 = cnt2 = 0

    for i in range(8):
        for j in range(8):
            if b[r+i][c+j] != chess_board1[i][j]:
                cnt1 += 1
            if b[r+i][c+j] != chess_board2[i][j]:
                cnt2 += 1
    
    return min(cnt1, cnt2)



N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_color = 987654321

# 범위 지정 주의하기
for i in range(len(board) - 7):
    for j in range(len(board[0]) - 7):
        color_num = recoloring(board, i, j)
        
        if min_color > color_num:
            min_color = color_num

print(min_color)