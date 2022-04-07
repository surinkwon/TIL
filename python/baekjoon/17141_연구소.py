'''
바이러스가 놓일 수 있는 칸을 조합해서 완전탐색
'''
from collections import deque
from itertools import combinations


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def findTime(lst):
    v = [[0] * N for _ in range(N)]
    q = deque()
    room = empty
    # 바이러스를 놓는 칸을 모두 큐에 추가(바이러스를 연구소에 놓음)
    for i in range(len(lst)):
        q.append(lst[i])
        v[lst[i][0]][lst[i][1]] = 1
        # 바이러스가 퍼지지 않은 빈칸
        room -= 1
    
    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            # 연구소 안이고 아직 안 퍼졌고 벽이 아니면 파이러스가 퍼짐
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and lab[nr][nc] != 1:
                q.append((nr, nc))
                v[nr][nc] = v[cr][cc] + 1
                room -= 1

    # 빈 칸이 남았으면 0 반환
    if room:
        return 0, 98765432
    else:
        # 바이러스를 모두 퍼뜨렸으면 최종 시간을 반환
        mt = 0
        for i in range(N):
            mt = max(max(v[i]), mt)
        return 1, mt - 1


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus_spot = []         # 바이러스를 놓을 수 있는 곳
can = False             # 바이러스를 놓을 수 있는 경우가 있는지
empty = 0               # 빈 칸
min_time = 98765432

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_spot.append((i, j))
        if lab[i][j] != 1:
            empty += 1

# 바이러스를 M개 놓을 수 있는 모든 경우의 수를 구함
possible = list(combinations(virus_spot, M))


for p in range(len(possible)):
    c, time = findTime(possible[p])
    # 바이러스를 모두 퍼뜨릴 수 있으면 최소 시간 갱신
    if c:
        min_time = min(min_time, time)
        can = True

if can:
    print(min_time)
else:
    print(-1)
