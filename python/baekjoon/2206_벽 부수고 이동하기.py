'''
벽이 있는 곳 정보를 받고 돌아가면서 하나씩 부수면서 최단 경로 찾음
중간에 최단경로보다 넘어가면 그만둠
(다익스트라?)

그냥 벽 있는 정보 받고 그 벽을 뚫고  처음부터 bfs돌고 다시 막고 다른 벽 꿇고 하는 것을 반복하니
시간초과가 났다. 

그래서 방문배열을 bfs돌 때마다 만들지 않고 전역변수로 두고 다음에 갈 곳이 지금 있는 곳 + 1(해당 장소까지의 거리)
보다 클 때만 방문하도록 하니 시간초과는 나지 않았는데 틀렸다.

그 이유는 시작점의 방문 정도가 1이고 거기에서 1씩 증가하는데 벽이 시작 바로 앞이 아니라 좀 가서 있으면
방문을 지금까지의 거리보다 더 큰 곳만 하도록 조건을 지정했기 때문에 가지를 못했다. 

그래서 그 다음엔 벽이 있는 곳을 시작으로 해서 bfs를 돌고 해당 지점의 방문 정도는 사방(거기에 올 수 있는 곳)에서 가장 작은 값 +1
을 한 값으로 지정했더니 테스트케이스가 제대로 돌아가지 않았다.

이 이유는 벽을 하나만 뚫을 수 있는데 아무 조건 없이 저렇게만 하면 앞에서 이미 막혀있는데도 
갈 수 있는 곳으로 처리를 해버려서 그렇다.

그래서 마지막으로 시작점에서 bfs로 갈 수 있는 곳을 다른 방문 배열에 저장한다음
이것을 기준으로 갈 수 있는지 없는지를 정하고 가도록 했다. 역시 시간초과가 났지만 pypy로 돌리니 통과했다.
(맨 처음 거는 pypy로 돌려도 시간 초과 나왔다.)

어떻게 하면 파이썬으로 돌려도 시간초과 안 나게 할 수 있을지 생각해봐야겠다.
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 방문배열을 따로 받아주는 이유는 시작 방문 배열을 따로 받아야하기 때문
def findWay(v, sr, sc):
    q = deque()
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        # 도착점에 도달했으면 걸린 시간 반환
        if r == N - 1 and c == M - 1:
            return v[r][c], v
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 내가 방문하려는 곳이 범위 내이며, 이전에 방문했을 때보다 지금 시간이 더 적게 들었으며, 벽이 아니면 방문
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] > v[r][c] +1 and place[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1
    
    return 9000000, v



N, M = map(int, input().split())
place = [list(map(int, input())) for _ in range(N)]
walls = []                                          # 벽 리스트
min_way = 9000000
visited = [[9000000] * M for _ in range(N)]         # 방문배열, 해당 지역을 방문할지 결졍할 때 지금보다 더 오래 걸렸을 때만 방문하게 했으므로 높은 수로 초기화
sv = [[9000000] * M for _ in range(N)]              # 시작 방문 배열

# 벽 위치 정보를 저장
for i in range(N):
    for j in range(M):
        if place[i][j]:
            walls.append((i, j))

# 벽이 있으면
if walls:
    # 일단 벽을 안 부수고 갈 수 있는 데까지 감
    sv[0][0] = 1
    min_way, sv = findWay(sv, 0, 0)

    # 벽을 하나씩 부수며 감
    for i in range(len(walls)):
        tmp = 9000000       # 네임에러 방지

        # 해당 벽이 다른 벽을 안 부숴도 갈 수 있는 벽인지 체크
        for delta in range(4):
            row, cal = walls[i][0] + dr[delta], walls[i][1] + dc[delta]

            # 만약 인덱스 범위 내이고(사방 중 하나라도), 시작점에서 벽을 안 부수고 올 수 있으면
            if 0 <= row < N and 0 <= cal < M and sv[row][cal] != 9000000:
                # 그 중 가장 작은 값에서 한 칸을 더 온 것이므로 1을 더해줌
                visited[walls[i][0]][walls[i][1]] = min(visited[walls[i][0]][walls[i][1]], sv[row][cal])
                visited[walls[i][0]][walls[i][1]] += 1

        # 만약 안 부수고 올 수 있었으면 거기서부터 bfs
        if visited[walls[i][0]][walls[i][1]] < 9000000:
            tmp, visited = findWay(visited, walls[i][0], walls[i][1])

        min_way = min(min_way, tmp)

# 벽이 하나도 없으면
else:
    min_way = N + M - 1
    

if min_way < 9000000:
    print(min_way)
else:
    print(-1)