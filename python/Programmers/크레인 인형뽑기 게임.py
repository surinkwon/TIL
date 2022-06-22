'''
인덱스 확인 잘 하기
'''

def solution(board, moves):
    answer = 0
    basket = []
    
    for i in range(len(moves)):
        cr, cc = 0, moves[i] - 1
        
        # 인형이 있는 곳까지 내려감
        while cr < len(board) and board[cr][cc] == 0:
            cr += 1
        
        # 인형이 있으면 잡아서 처리
        if cr < len(board):
            doll = board[cr][cc]
            if not basket:
                basket.append(doll)
            else:
                if basket[-1] == doll:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(doll)
                
            board[cr][cc] = 0
            
    return answer