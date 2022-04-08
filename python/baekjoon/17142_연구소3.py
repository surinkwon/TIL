'''
활성화시킬 바이러스를 고를 모든 경우의 수를 구함
모든 경우를 돌면서 최소시간을 구함

연구소 2와 다른점
- 바이러스는 그곳에 있지만 활성화가 되지 않았을 뿐
- 즉 연구소 2는 아예 처음부터 바이러스가 단 M개의 곳에만 놓여지는 것인데 연구소 3은 바이러스가 비활성화 된 상태라서 
  비활성화된 바이러스가 있는 곳도 이미 바이러스가 퍼진 것으로 간주함.
- 연구소 2에서는 바이러스가 놓일 수 있는 자리가 표시된 거고 지금 문제는 바이러스들은 이미 있지만 활성, 비활성만 나뉜 것

- 그래서 연구소 2랑 비슷하게 풀면 되지만 조금만 다르게 해주면 됨
- 연구소 2에서는 빈 곳을 2가 표시된 곳도 세줬지만 여기에서는 0이 있는 곳만 세어줌
  나중에 시간이 얼마나 걸렸는지 보는 것도 원래 바이러스가 있던 자리는 빼고 검사
'''
from collections import deque
from itertools import combinations


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def spread(lst, rest):
    q = deque()
    v = [[0] * N for _ in range(N)]
    # 바이러스 활성화
    for i in range(len(lst)):
        q.append(lst[i])
        v[lst[i][0]][lst[i][1]] = 1

    while q:
        cr, cc = q.popleft()
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            
            # 연구실 안이고 아직 방문하지 않은 곳이며 벽이 아니면 방문
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and lab[nr][nc] != 1:
                # 원래 바이러스가 있던 자리가 아니면 남은 공간 -1
                if lab[nr][nc] == 0:
                    rest -= 1
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1

    if rest:
        return 0, 0
    else:
        # 바이러스가 있던 자리는 보지 않고 걸린 시간을 구함
        mt = 0
        for r in range(N):
            for c in range(N):
                if lab[r][c] == 0:
                    mt = max(mt, v[r][c])
        return 1, mt - 1


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus_place = []                        # 바이러스가 있는 자리
empty = 0                               # 빈 공간
min_time = 98765432
can = False
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_place.append((i, j))
        if lab[i][j] == 0:              # 바이러스도 없고 벽도 아니면 빈 공간 세어줌
            empty += 1

# 빈 공간이 없으면 => 모두 벽이거나 바이러스가 다 차있으면
if empty == 0:
    can = True
    min_time = 0
# 빈 공간이 있으면
else:
    # 활성화 시킬 수 있는 경우를 모두 찾음
    possible = list(combinations(virus_place, M))

    # 모든 경우를 돌면서 최소시간 찾음
    for p in range(len(possible)):
        c, time = spread(possible[p], empty)

        if c:
            can = True
            min_time = min(min_time, time)

if can:
    print(min_time)
else:
    print(-1)


