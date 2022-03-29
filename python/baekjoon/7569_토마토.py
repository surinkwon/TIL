from collections import deque


dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def howLong(ripe_lst):
    global under_ripe_tomato
    v = [[[0] * M for _ in range(N)] for __ in range(H)]
    q = deque()
    
    for i in range(len(ripe_lst)):
        q.append(ripe_lst[i])
        v[ripe_lst[i][0]][ripe_lst[i][1]][ripe_lst[i][2]] = 1
    
    while q:
        h, r, c = q.popleft()

        if under_ripe_tomato == 0:
            # q끝까지 돈 경우 위에서 이미 pop했기 때문에 q에 원소가 없을 수 있다
            # 따라서 q가 비었는지 안 비었는지 체크하고 빼야 함
            if len(q):
                # 끝에 있는 걸 빼는 이유는 방문 처리를 할 때 이미 익었다고 체크하기 때문에
                # 사실 큐에서 빼는 토마토가 익었을 때 모든 토마토가 익지는 않았을 수 있는데 다 익었다고 간주되는 경우가 있음
                # 따라서 그런 경우를 고려해 가장 마지막을 빼줌
                h, r, c = q.pop()
            return v[h][r][c] - 1
        
        for d in range(6):
            nh = h + dh[d]
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if box[nh][nr][nc] == 0 and v[nh][nr][nc] == 0:
                    q.append((nh, nr, nc))
                    v[nh][nr][nc] = v[h][r][c] + 1
                    under_ripe_tomato -= 1

    return -1



M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
ripe_tomato = []
under_ripe_tomato = 0

# 익은 토마토 찾기, 안 익은 토마토 개수 세기
for height in range(H):
    for i in range(N):
        for j in range(M):
            if box[height][i][j] == 1:
                ripe_tomato.append((height, i, j))
            elif box[height][i][j] == 0:
                under_ripe_tomato += 1

# bfs
rlt = howLong(ripe_tomato)

print(rlt)