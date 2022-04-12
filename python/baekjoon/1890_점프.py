'''
갈 수 있는 경로에 여태까지 올 수 있었던 경로 수를 더해줌
DP
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 시작지점이면
        if i == j == 0:
            rignt_col = j + board[i][j]
            down_row = i + board[i][j]
            # 오른쪽으로 갈 수 있으면
            if rignt_col < N:
                # 해당 칸에 1 더함
                v[i][rignt_col] = 1
            # 아래로 갈 수 있으면
            if down_row < N:
                # 해당 칸에 1 더함
                v[down_row][j] = 1
        else:
            # 해당 칸에 올 수 있었고 점프도 할 수 있으면
            if v[i][j] and board[i][j]:
                rignt_col = j + board[i][j]
                down_row = i + board[i][j]
                # 오른쪽, 아래 방향 검사해서 갈 수 있으면 현재 칸까지 올 수 있던 경로 수를 더해줌
                if rignt_col < N:
                    v[i][rignt_col] += v[i][j]
                if down_row < N:
                    v[down_row][j] += v[i][j]


print(v[N-1][N-1])