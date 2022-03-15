import sys

sys.stdin = open('input.txt')

T = 10

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# bfs함수
def bfs(m, s):
    visited = [[0] * len(m) for _ in range(len(m))]
    queue = [0] * (len(m) ** 2)
    qf = qr = -1
    qr += 1
    # 큐의 첫번째에 시작점을 넣고 시작점을 방문 처리 해줌
    queue[qr] = s
    visited[s[0]][s[1]] = 1
    
    # 갈 곳이 있을 때까지
    while qr != qf:
        qf += 1
        
        # 새로운 출발점의 행, 열
        r = queue[qf][0]
        c = queue[qf][1]
        
        # 도착점에 다다랐으면 1 반환
        if m[r][c] == 3:
            return 1
        
        # 도착점이 아니면 해당 출발점에서 갈 수 있는 곳을 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 가려는 곳이 미로 범위 내이고 방문하지 않았으며 벽이 아니면 큐에 넣어주고 방문처리
            # m[nr][nc] == 0으로 조건을 걸면 도착점에 절대 도달할 수 없기 때문에 유의할 것
            if 0 <= nr < len(m) and 0 <= nc < len(m) and visited[nr][nc] == 0 and m[nr][nc] != 1:
                qr += 1
                queue[qr] = (nr, nc)
                visited[nr][nc] = 1

    return 0


for tc in range(1, T + 1):
    tcc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    
    # 출발점 찾기
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                start = (i, j)
                break

    rlt = bfs(maze, start)

    print(f'#{tc} {rlt}')

