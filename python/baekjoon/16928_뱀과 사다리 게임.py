'''
bfs
'''
from collections import deque

def shortCut(n):
    q = deque()
    v = [0] * 101
    q.append(n)
    v[n] = 1

    while q:
        cn = q.popleft()

        if cn == 100:
            return v[cn] - 1

        for d in range(6, 0, -1):
            if cn + d <= 100:
                if board[cn+d] == 0 and v[cn+d] == 0:
                    q.append(cn+d)
                    v[cn+d] = v[cn] + 1
                elif board[cn+d] and board[cn+d][0] == 'L' and v[cn+d] == 0:
                    q.append(board[cn+d][1])
                    v[cn+d] = v[cn] + 1
                    if v[board[cn+d][1]] == 0:
                        v[board[cn+d][1]] = v[cn] + 1
                elif board[cn+d] and board[cn+d][0] == 'S' and v[cn+d] == 0:
                    q.append(board[cn+d][1])
                    v[cn+d] = v[cn] + 1
                    # 아래 조건을 주지 않으면 방문 횟수가 달라질 수 있음(이전에 방문했던 곳을 바꿀 수도 있기 때문)
                    if v[board[cn+d][1]] == 0:
                        v[board[cn+d][1]] = v[cn] + 1


N, M = map(int, input().split())
board = [0] * 101

for _ in range(N):
    ladder_s, ladder_e = map(int, input().split())
    board[ladder_s] = ['L', ladder_e]

for _ in range(M):
    snake_s, snake_e = map(int, input().split())
    board[snake_s] = ['S', snake_e]

rlt = shortCut(1)

print(rlt)