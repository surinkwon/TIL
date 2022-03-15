# bfs 탐색 함수
def findWay(m, start, end):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[0] * len(m[0]) for _ in range(len(m))]
    queue = [0] * (len(m[0]) * len(m))
    f = r = -1
    r += 1
    queue[r] = start
    visited[start[0]][start[1]] = 1

    while f != r:
        f += 1
        row = queue[f][0]
        col = queue[f][1]

        if row == end[0] and col == end[1]:
            return visited[row][col]
        
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]

            if 0 <= nr < len(m) and 0 <= nc < len(m[0]):
                if m[nr][nc] and visited[nr][nc] == 0:
                    r += 1
                    queue[r] = (nr, nc)
                    visited[nr][nc] = visited[row][col] + 1
    
    return 0


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
start = (0, 0)
end = (N - 1, M - 1)

min_d = findWay(maze, start, end)

print(min_d)