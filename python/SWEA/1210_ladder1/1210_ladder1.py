import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    # tc
    num = int(input())
    # 사다리
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 마지막이 2인 좌표에서 사다리타고 위로 올라옴
    # 2인 좌표값 r, c
    for end in range(len(ladder[99])):
        if ladder[99][end] == 2:
            r = 99
            c = end

    # 움직이는 방향
    up, right, left = -1, 1, -1

    while 0 <= r and 0 <= c < len(ladder[0]): # 인덱스 범위 내에서
        # 현재 열의 오른쪽으로 통로가 있다면
        # bc <= c를 안 하면 elif 문을 돌면서 다시 왼쪽으로 가기 때문에
        # 내가 타고 온 줄이 통로 끝의 줄보다 작거나 같은 열에 있다는 조건을 넣어 줘야 함
        if c + right < len(ladder[0]) and ladder[r][c + right] and bc <= c:
            c += right
            continue
        # 현재 열의 왼쪽으로 통로가 있다면
        elif c + left >= 0 and ladder[r][c + left] and bc >= c:
            c += left
            continue

        r += up
        bc = c

        if r == 0:
            start_point = c

    print(f'#{tc} {start_point}')

