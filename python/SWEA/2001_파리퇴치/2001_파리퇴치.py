import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    # 공간, 파리채 크기
    N, M = map(int, input().split())
    # 공간에 있는 파리 수
    fly = [list(map(int, input().split())) for _ in range(N)]

    # 파리채로 잡는 파리 수 / 파리채로 잡을 수 있는 최대 파리
    each = 0
    max_fly = 0
    # 파리채 크기를 포함해서 공간을 넘지 않을 때까지
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            # 파리채 면적만큼 파리 수 합산
            each = 0
            for i in range(M):
                for j in range(M):
                    each += fly[r+i][c+j]

            if max_fly < each:
                max_fly = each

    print(f'#{tc} {max_fly}')

