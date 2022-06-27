def solution(rows, columns, queries):
    board = []
    answer = []

    # 숫자 판 만들기
    for i in range(1, rows * columns, columns):
        board.append([j for j in range(i, i + columns)])
    
    # 각 쿼리 수행
    for i in range(len(queries)):
        x1, y1, x2, y2 = queries[i]
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        tmp = []
        
        # 모서리 수들
        fst = board[x1][y2]
        snd = board[x2][y2]
        trd = board[x2][y1]
        
        # 회전
        for c in range(y2, y1, -1):
            board[x1][c] = board[x1][c - 1]
            tmp.append(board[x1][c - 1])
        
        for r in range(x2, x1, -1):
            board[r][y2] = board[r - 1][y2]
            tmp.append(board[r - 1][y2])
        
        for c in range(y1, y2):
            board[x2][c] = board[x2][c + 1]
            tmp.append(board[x2][c + 1])
        
        for r in range(x1, x2):
            board[r][y1] = board[r + 1][y1]
            tmp.append(board[r + 1][y1])
        
        board[x1 + 1][y2] = fst
        board[x2][y2 - 1] = snd
        board[x2 - 1][y1] = trd
        
        # 회전시킨 숫자들 중 가장 작은 수를 배열에 추가
        answer.append(min(min(tmp), fst, snd, trd))
    
    return answer