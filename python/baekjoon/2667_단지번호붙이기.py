# BFS 함수
def findWay(m, start):
    """
    단지 내 집 개수를 구하는 함수

    :param m: 지도
    :param start: 단지 내에 존재하는 집의 좌표
    :return m: 변형된 지도
    :return t - 1: 단지 내 집 개수
    """
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
        t += 1 # 방문하면 집 개수를 세어줌
        
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]

            if 0 <= nr < len(m) and 0 <= nc < len(m[0]):
                if m[nr][nc] and visited[nr][nc] == 0:
                    r += 1
                    queue[r] = (nr, nc)
                    m[nr][nc] = 0 # 재방문하면 안 되므로 지도를 변경
    
    return m, t - 1

# 지도 내 모든 단지 수와 집 개수를 찾는 함수
def estate(matrix):
    estates = []
    estate_num = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                # 지도를 돌다 집이 있으면 집 개수를 찾음
                matrix, num = findWay(matrix, (i, j))
                # 찾은 집 개수를 집 수 리스트에 추가
                estates.append(num)
                estate_num += 1 # 단지 수 증가시킴
    
    # 단지 수, 단지별 집 수 리스트
    return estate_num, estates



N = int(input())

apart = [list(map(int, input())) for _ in range(N)]

total, houses = estate(apart)
houses.sort()

print(total)
for i in range(len(houses)):
    print(houses[i])
