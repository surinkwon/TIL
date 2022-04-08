'''
bfs로 물고기를 먹으러 가는데
가장 빨리 도착한 칸에 먹을 수 있는 물고기가 있으면 먹고 큐 초기화
방문 배열도 초기화
방향은 위, 왼쪽을 먼저 둠

원래는 방향배열을 상, 좌, 우, 하로 둬서 bfs 한 번만 돌리고 풀려고 했는데 이렇게 해도 정확한 답이 나오지는 않았다.
왼쪽 아래에 있으면 오른쪽에 있는 것보다 더 빨리 닿기 때문에... 틀린 답이 나왔다
그래서 가까운 먹이들의 좌표를 저장하고 정렬해서 가장 앞에 있는 것을 먹고 다시 bfs를 돌리는 식으로 짰다.
'''
from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def eatFish(st, size):
    global sea
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append(st)
    v[st[0]][st[1]] = 1
    can_eat = []
    # 걸리는 시간(반환 값)
    time = 9876543

    while q:
        cr, cc = q.popleft()

        # 물고기가 있고 크기가 상어보다 작으며 해당 장소까지 도달하는 시간이 이전에 도착했을 때보다
        # 작거나 같을 때(동일한 시간에 도착해서 먹을 수 있는 먹이의 좌표를 모두 반환해야하기 때문에)
        if sea[cr][cc] and sea[cr][cc] < size and v[cr][cc] <= time:
            can_eat.append((cr, cc))
            # 최초로 먹이를 먹을 수 있는 곳에 도달했으면 시간을 갱신해줘야 함
            # 맨 처음에 큰 값으로 했기 때문
            if time > v[cr][cc]:
                time = v[cr][cc]
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            
            # 범위 내이고 크기가 같거나 작으면 이동
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and sea[nr][nc] <= size:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1
    
    # 만약 먹을 수 있는 먹이가 없으면 혹은 먹으러 갈 수 없으면 0을 반환해줘야하므로
    # 시간을 1로 초기화해줌
    if time == 9876543:
        time = 1

    # 최소 이동 시간, 먹이 좌표 리스트 반환
    return time - 1, can_eat


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
rlt = fish_cnt = 0
size = 2
t = 1

# 시작 상어 위치 저장
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            start = [i, j]

# 먹을 수 있는 먹이가 있으면(t값이 0이라는 것은 먹을 수 있는 먹이가 없다는 것)
while t:
    t, fish = eatFish(start, size)
    if fish:
        # 거리가 같은 먹이가 있으면 우측, 좌측 순으로 먼저 가야하므로 정렬해줌
        # 맨 앞의 먹이가 결국 먹는 먹이가 됨
        fish.sort(key=lambda x:(x[0], x[1]))
        
        # 먹이 먹기
        fish_cnt += 1
        sea[fish[0][0]][fish[0][1]] = 0

        # 상어 성장
        if fish_cnt == size:
            fish_cnt = 0
            size += 1
        
        # 다시 현재 먹이를 먹은 위치부터 먹이 탐색
        start = [fish[0][0], fish[0][1]]
    
    # 걸린 시간 증가
    rlt += t

print(rlt)