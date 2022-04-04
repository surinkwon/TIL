'''
dfs로 푸는 풀이
dfs로 풀면 ㅗ자 빼고는 다 검사 가능
파이선으로 돌리니까 시간초과...
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
rest_dr = [1, 1, -1, -1]
rest_dc = [1, -1, -1, 1]

def findMaxSum(r, c, num, s):
    global max_sum, v
    if num == 3:
        if max_sum < s:
            max_sum = s
    else:
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:
                v[nr][nc] = 1
                findMaxSum(nr, nc, num+1, s+board[nr][nc])
                v[nr][nc] = 0


# ㅗ 자 구하는 함수
def rest(r, c):
    global max_sum

    for d in range(4):
        s = board[r][c]
        for p in range(1, 4):
            if p == 3:
                break

            nr, nc = r + dr[d]*p, c + dc[d]*p
            if 0 <= nr < N and 0 <= nc < M:
                s += board[nr][nc]
            else:
                break
        
        if p == 3:
            nr, nc = r + rest_dr[d], c + rest_dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                s += board[nr][nc]

                if max_sum < s:
                    max_sum = s


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        findMaxSum(i, j, 0, board[i][j])
        v[i][j] = 0

        rest(i, j)

print(max_sum)
