'''
DFS
셋으로 해도 시간초과, 딕셔너리로 해도 시간초과 남
룩업리스트 만들어서 푸니 시간초과 안 남
'''
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
alph = [0] * 26


def howFar(r, c, move):
    global max_move
    if max_move < move:
        max_move = move
    elif max_move == 26:
        return
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if max_move == 26:
            return
        elif 0 <= nr < R and 0 <= nc < C and alph[ord(board[nr][nc]) - 65] == 0:
            alph[ord(board[nr][nc]) - 65] = 1
            howFar(nr, nc, move+1)
            alph[ord(board[nr][nc]) - 65] = 0

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
max_move = 1
alph[ord(board[0][0]) - 65] = 1

howFar(0, 0, 1)

print(max_move)