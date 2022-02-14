# 높이, 너비
M, N = map(int, input().split())
snail = [[0] * N for _ in range(M)]
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = r = c = 0
i = 0
final = 1

while final < M * N + 1:
    snail[r][c] = final
    if 0 <= r + dr[i] < M and 0 <= c + dc[i] < N and snail[r+dr[i]][c+dc[i]] == 0:
        pass
    else:
        cnt += 1
    
    i = cnt % 4
    r += dr[i]
    c += dc[i]
    final += 1

print(cnt-1)