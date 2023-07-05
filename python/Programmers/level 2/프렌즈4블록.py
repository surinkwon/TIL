'''
그대로 구현
'''

def solution(m, n, board):
    answer = 0
    new_board = [list(board[i]) for i in range(len(board))]
    block_num = 1
    
    # 지울 블록 자리를 찾는 함수
    def removeBlocks(r, c, b):
        nonlocal tmp
        for nr in range(r, r+2):
            for nc in range(c, c+2):
                if new_board[nr][nc] != b:
                    return
        
        for i in range(r, r+2):
            for j in range(c, c+2):
                tmp.add((i, j))
        return

    # 블록을 지운 후 처리를 하는 함수
    def after():
        nonlocal new_board

        # 빈 자리가 있으면 블록을 아래로 내려서 채움
        for c in range(n):
            for r in range(m-1, -1, -1):
                if new_board[r][c] == 0:
                    cr = r
                    while r > -1 and new_board[r][c] == 0:
                        r -= 1
                    if r > -1:
                        new_board[cr][c] = new_board[r][c]
                        new_board[r][c] = 0
    
    # 지울 블록이 있는 동안
    while block_num:
        tmp = set()

        # 게임판을 돌며 지울 블록 찾음
        for i in range(m-1):
            for j in range(n-1):
                if new_board[i][j]:
                    removeBlocks(i, j, new_board[i][j])

        block_num = len(tmp)                    # 지울 블록 개수
        tmp = list(tmp)
        answer += block_num
        for b in range(len(tmp)):               # 블록 지우기
            new_board[tmp[b][0]][tmp[b][1]] = 0
        after()                                 # 후처리
                
    return answer

a = solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
print(a)