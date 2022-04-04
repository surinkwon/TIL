'''
룩업 테이블 만들어서 풀기(인덱스 사이의 규칙을 찾아서 만들 수 있다)
룩업 테이블이 아니라 dfs돌게 하면 시간초과
사실 이것도 파이썬으로 돌리면 시간초과 나는데 파이파이로 돌려서 풀었다...
'''

def nQueen(row):
    global cnt
    if row == N:
        cnt += 1
    else:
        for i in range(N):
            if table_col[i] == table_ldi[row-i+N] == table_rdi[row+i] == 0:
                table_col[i] = table_ldi[row-i+N] = table_rdi[row+i] = 1
                nQueen(row+1)
                table_col[i] = table_ldi[row-i+N] = table_rdi[row+i] = 0

N = int(input())
table_col = [0] * N
table_rdi = [0] * (2 * N)
table_ldi = [0] * (2 * N)
cnt = 0
nQueen(0)
print(cnt)