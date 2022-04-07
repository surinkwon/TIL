'''
치즈의 바깥을 bfs로 체크하면서 치즈의 경계 부분을 0으로 만들어주고 동시에 방문처리
치즈가 없어질 때까지 반복

중요
- bfs를 꼭 무언가 있는 데에서만 돌려고 생각하지 말 것
- 계속 치즈가 있는 부분을 bfs로 돌 생각을 해서 어떻게 경계를 찾아야할지 막막했는데
  치즈가 아닌 부분을 돌 수 있다는 생각을 하고서는 풀이가 빨리 생각났다
- 생각을 한정시키지 말자
'''
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def meltCheese(r, c):
    global cheese_size, plate
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            # 범위 내이면서 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:
                # 만약 치즈가 없는 부분이면 계속 돌아야하므로 큐에 넣어줌
                if plate[nr][nc] == 0:
                    q.append((nr, nc))
                    v[nr][nc] = 1
                # 치즈의 경계부분이면 치즈를 녹였는데 다시 큐에 넣으면 경계만 녹일 수 없으므로
                # 큐에는 넣지 않음
                elif plate[nr][nc]:
                    v[nr][nc] = 1
                    plate[nr][nc] = 0
                    cheese_size -= 1

N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
cheese_size = 0
time = 0
last_cheese_size = 0

for i in range(N):
    for j in range(M):
        if plate[i][j]:
            cheese_size += 1

# 치즈가 다 녹을 때까지 반복
while cheese_size > 0:
    # 치즈가 녹기 한 시간 전 크기를 구해야하므로 위에서 체크
    # bfs를 돌면서 치즈가 다 녹아버리면 반복문을 돌지 않기 때문에 한 시간 전 크기를 구할 수 있음
    last_cheese_size = cheese_size
    meltCheese(0, 0)
    time += 1

print(time)
print(last_cheese_size)
