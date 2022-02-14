import sys

sys.stdin = open('input.txt')

T = int(input())

def snail(N):
    # N에 따른 이차원 배열
    snail_lst = [[0] * N for _ in range(N)]
    # 방향들
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    num = 1 # 시작하는 수
    r = c = td = cs = 0 # 행, 열, 방향, 숫자가 있는 맨 왼쪽 열
    rs = 1 # 숫자가 있는 맨 위 행
    re = ce = N # 숫자가 있는 맨 아래 행, 맨 오른쪽열
    while num < N ** 2 + 1: # 수가 다 채워질 때까지
        # 각 방향을 나누어 조건 지정
        if td == 0: # 오른쪽으로 갈 때
            if c >= ce:
                td = 1
                ce -= 1
                c -= 1
            else:
                snail_lst[r][c] = num
                num += 1

        elif td == 2: # 아래로 갈 때
            if c < cs:
                td = 3
                cs += 1
                c += 1
            else:
                snail_lst[r][c] = num
                num += 1

        elif td == 1: # 왼쪽으로 갈 때
            if r >= re:
                td = 2
                re -= 1
                r -= 1
            else:
                snail_lst[r][c] = num
                num += 1

        else: # 위로 갈 때
            if r < rs:
                td = 0
                rs += 1
                r += 1
            else:
                snail_lst[r][c] = num
                num += 1

        r += dr[td]
        c += dc[td]

    return snail_lst


for tc in range(1, T + 1):
    a = snail(int(input()))

    print(f'#{tc}')
    for line in a:
        for number in line:
            print(number, end=' ')
        print()

