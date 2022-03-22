from collections import deque

'''
물이 가는 길을 먼저 표시하고 고슴도치가 출발하는 방식으로 구현
고슴도치는 물이 차있거나 찰 예정인 곳을 갈 수 없으므로, 고슴도치가 갈 때는
인접 칸의 숫자가 자신의 칸 숫자 + 1보다 큰 칸의 경우만 가도록 함
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def waterBfs(loc):
    v = [[0] * len(woods[0]) for _ in range(len(woods))]
    q = deque()

    for i in range(len(loc)):
        q.append(loc[i])
        v[loc[i][0]][loc[i][1]] = 1
    
    while q:
        cr, cc = q.popleft()
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < len(v) and 0 <= nc < len(v[0]):
                if woods[nr][nc] != 'X' and woods[nr][nc] != 'D' and v[nr][nc] == 0:
                    q.append([nr, nc])
                    v[nr][nc] = v[cr][cc] + 1
    
    return v

def hedgehogBfs(s):
    v = [[0] * len(woods[0]) for _ in range(len(woods))]
    v[s[0]][s[1]] = 1
    q = deque()
    q.append(s)

    while q:
        cr, cc = q.popleft()

        if woods[cr][cc] == 'D':
            return v[cr][cc] - 1
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < len(v) and 0 <= nc < len(v[0]):
                if woods[nr][nc] != 'X' and visited[nr][nc] > v[cr][cc] + 1 and v[nr][nc] == 0:
                    q.append([nr, nc])
                    v[nr][nc] = v[cr][cc] + 1

    return 'KAKTUS'


N, M = map(int, input().split())
woods = [list(input()) for _ in range(N)]
water = []
for i in range(len(woods)):
    for j in range(len(woods[0])):
        if woods[i][j] == '*':
            water.append([i, j])
        elif woods[i][j] == 'S':
            start = [i, j]

visited = waterBfs(water)

for i in range(len(woods)):
    for j in range(len(woods[0])):
        if woods[i][j] != 'X' and visited[i][j] == 0:
            visited[i][j] = 987654321

rlt = hedgehogBfs(start)

print(rlt)

