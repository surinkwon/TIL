'''
설명대로 구현

주의할 점
- 설명된 차례대로 구현해야 답이 맞는다.
(실행 횟수를 줄여보려고 구름 하나를 이동시킨 후 물의 양을 증가시키고 대각선 검사해서 물복사 마법까지 실행한 후
다음 구름을 이동시켜서 같은 일을 반복하도록 했는데 이렇게 하면 물복사가 제대로 일어나지 않는다. 
대각선 방향에 현재 물이 없더라도 그곳에 구름이 있으면 물이 증가되기 때문에 현재 위치에 물 증갸량이 다를 수도 있다.)
- 인덱스 주의(8까지 검사하고싶으면 9를 적어줘야 한다. 조심좀)
'''

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 격자 크기, 이동 횟수
N, M = map(int, input().split())

# 격자
matrix = [list(map(int, input().split())) for _ in range(N)]

# 구름
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

# M번의 이동
for _ in range(M):
    # 방향, 칸 수
    d, n = map(int, input().split())

    # 1. 모든 구름이 해당 방향으로 칸 수만큼 이동
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dr[d] * n) % N
        cloud[i][1] = (cloud[i][1] + dc[d] * n) % N

        # 2. 구름이 있는 자리의 물의 양 + 1
        matrix[cloud[i][0]][cloud[i][1]] += 1

    for i in range(len(cloud)):
        # 4. 물이 증가한 칸에 물복사 마법
            # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 물 증가
        for de in range(2, 9, 2):
            r, c = cloud[i][0] + dr[de], cloud[i][1] + dc[de]
            if 0 <= r < N and 0 <= c < N and matrix[r][c]:
                matrix[cloud[i][0]][cloud[i][1]] += 1

    # 5. 물의 양이 2 이상인 모든 칸에 구름 생김(구름이 사라진 칸 제외)
    pre_cloud = set([tuple(cloud[n]) for n in range(len(cloud))])
    cloud = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 1 and (i, j) not in pre_cloud:
                cloud.append([i, j])
                matrix[i][j] -= 2

total_water = [sum(matrix[i]) for i in range(len(matrix))]
print(sum(total_water))


