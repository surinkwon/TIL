'''
그대로 구현
달팽이 처럼 하면 됨

토네이도는 격자의 처음칸에 오기 전에 1부터 N - 1의 길이를 각각 두번 씩 돌게 된다.(N - 1 길이만 3번)
다시말하면 1만큼 움직인 후 방향을 틀고 또 1만큼 움직이고 방향을 튼 다음
같은 방향으로 2만큼 움직이고 방향을 바꾸고 다시 2만큼 그 방향으로 움직이고 방향을 바꾼다. 
이렇게 N - 1까지 반복
이를 이용해서 구현하면 된다.
'''

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 토네이도가 움직이는 방향에 따라 흩날리는 먼지들의 좌표를 해당 퍼센트와 맞는 인덱스에 담아놓음
percent = [
    [0, [(-1, 1), (1, 1)], [(-2, 0), (2, 0)], 0, 0, [(0, -2)], 0, [(-1, 0), (1, 0)], 0, 0, [(-1, -1), (1, -1)]],
    [0, [(-1, -1), (-1, 1)], [(0, -2), (0, 2)], 0, 0, [(2, 0)], 0, [(0, -1), (0, 1)], 0, 0, [(1, 1), (1, -1)]],
    [0, [(-1, -1), (1, -1)], [(-2, 0), (2, 0)], 0, 0, [(0, 2)], 0, [(-1, 0), (1, 0)], 0, 0, [(-1, 1), (1, 1)]],
    [0, [(1, -1), (1, 1)], [(0, -2), (0, 2)], 0, 0, [(-2, 0)], 0, [(0, -1), (0, 1)], 0, 0, [(-1, 1), (-1, -1)]],
]


# 모래를 움직이는 함수
def moveSand(tr, tc):
    global total, metrix
    sr, sc = tr + dr[d], tc + dc[d]                             # 모래의 좌표
    sand = metrix[sr][sc]                                       # 모래의 양
    if sand:                                                    # 모래가 있으면 모래를 옮기고 없으면 그냥 이동
        metrix[sr][sc] = 0                                      # 모래는 어차피 다른 곳으로 다 이동할 것이기 때문에 해당 칸의 모래를 없앰
        spread = 0                                              # 확률이 써진 방향으로 퍼지는 모래의 양
        for per in range(1, 11):                                # 확률이 10%까지 있기 때문에 범위를 10까지로 조정
            if percent[d][per]:
                for coor in range(len(percent[d][per])):        # 해당 확률의 칸수만큼
                    percoor = percent[d][per][coor]
                    r, c = sr + percoor[0], sc + percoor[1]     # 각 칸의 좌표를 구하고

                    if 0 <= r < N and 0 <= c < N:               # 좌표가 격자 범위 내이면
                        metrix[r][c] += (sand * per) // 100     # 해당 좌표에 모래 퍼뜨리고
                        spread += (sand * per) // 100           # 퍼진 모래 양 저장
                    else:
                        total += (sand * per) // 100            # 격자 밖이면 밖으로 떨어뜨림
                        spread += (sand * per) // 100

        nsr , nsc = sr + dr[d], sc + dc[d]                      # 남은 모래가 이동할 좌표
        sand -= spread                                          # 모래는 확률칸에 퍼뜨리고 남은 양
        if 0 <= nsr < N and 0 <= nsc < N:                       # 격자 범위 내이면 그곳으로 옮기고
            metrix[nsr][nsc] += sand
        else:                                                   # 격자 범위 밖이면 떨어뜨림
            total += sand
    
    return sr, sc



N = int(input())
metrix = [list(map(int, input().split())) for _ in range(N)]
total = 0           # 격자 밖으로 떨어지는 모래
tr = tc = N // 2    # 토네이도 처음 시작 위치
cnt = 1             # 토네이도 경로 결정을 위한 변수
d = 0               # 토네이도 방향

while tr > 0 or tc > 0:
    # cnt가 격자 크기와 같아지면 이전 길이만큼 한 번 더 돌기 때문에 하나 줄여줌
    if cnt == N:
        cnt -= 1

    # cnt만큼 동일한 방향으로 이동
    for i in range(cnt):
        # 이동하면서 모래를 옮김
        tr, tc = moveSand(tr, tc)

    # 토네이도가 격자의 시작점에 도달하면 끝남
    if tr == 0 and tc == 0:
        break

    # 방향 전환
    d = (d + 1) % 4

    # 다시 cnt만큼 동일한 방향으로 이동
    for i in range(cnt):
        tr, tc = moveSand(tr, tc)

    # 다시 방향 전환
    d = (d + 1) % 4
    cnt += 1

print(total)


