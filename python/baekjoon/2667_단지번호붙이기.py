def findWay(m, start):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[0] * len(m[0]) for _ in range(len(m))]
    queue = [0] * (len(m[0]) * len(m))
    f = r = -1
    r += 1
    queue[r] = start
    visited[start[0]][start[1]] = 1
    m[start[0]][start[1]] = 0
    t = 1

    while f != r:
        f += 1
        row = queue[f][0]
        col = queue[f][1]
        t += 1
        
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]

            if 0 <= nr < len(m) and 0 <= nc < len(m[0]):
                if m[nr][nc] and visited[nr][nc] == 0:
                    r += 1
                    queue[r] = (nr, nc)
                    m[nr][nc] = 0
    
    return m, t - 1

def estate(matrix):
    estates = []
    estate_num = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                matrix, num = findWay(matrix, (i, j))
                estates.append(num)
                estate_num += 1
    
    return estate_num, estates



N = int(input())

apart = [list(map(int, input())) for _ in range(N)]

total, houses = estate(apart)
houses.sort()

print(total)
for i in range(len(houses)):
    print(houses[i])
