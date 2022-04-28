'''
행, 열은 따로 배열을 만들어서 세주고 5가 되면 해당 수 출력
행 == 열이거나 행 == N(5) - 열 -1 이면 대각선도 세어줌
'''

def whatNum():
    row_b = [0] * 5             # 행 빙고 검사 배열
    col_b = [0] * 5             # 열 빙고 검사 배열
    l_dig = r_dig = 0           # 대각선 빙고 검사
    num_cnt = line_cnt = 0
    for i in range(5):
        for j in range(5):
            num_cnt += 1        # 수를 부름
            for r in range(5):
                for c in range(5):

                    # 부른 수와 같은 수를 지우고 처리
                    if numbers[i][j] == board[r][c]:
                        # 대각선 처리
                        if r == c:
                            l_dig += 1
                        if r == 5 - c - 1:
                            r_dig += 1
                        
                        # 행, 열 처리
                        row_b[r] += 1
                        col_b[c] += 1
                        
                        # 행과 열이 빙고된 줄이 있는지 체크
                        # 한 번 빙고가 된 행이나 열은 다시 부르지 않으므로 이렇게 해줘도 됨
                        if row_b[r] == 5:
                            line_cnt += 1
                        if col_b[c] == 5:
                            line_cnt += 1
                        if l_dig == 5:
                            line_cnt += 1
                            l_dig = 0       # 대각선은 한 번 빙고 처리를 해줬으면 다음부터는 따로 더해주면 안 됨
                        if r_dig == 5:
                            line_cnt += 1
                            r_dig = 0
            
            if line_cnt >= 3:
                return num_cnt

board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]

rlt = whatNum()

print(rlt)
