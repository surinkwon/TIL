import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    # 퍼즐 크기, 단어 길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    space = 0

    # 가로랑 세로를 나누어 조건 설정

    # 퍼즐을 한 칸씩 돌면서
    for r in range(N):
        for c in range(N):
            if puzzle[r][c] == 1:
                cnt_r = cnt_c = 0
                # 가로로 검사, 시작점은 행의 맨 처음 혹은 이전 열이 막힌 곳이어야 함
                if c == 0 or puzzle[r][c-1] == 0:
                    for nc in range(1, N-c): # 지금 열에서 마지막 열까지
                        if puzzle[r][c+nc]: # 빈 공간을 만나면 + 1
                            cnt_c += 1
                        else:
                            break # 막혀있으면 빠져나옴

                    # 퍼즐의 칸이 빈 공간일 때 검사를 시작한 것이므로
                    # 빈 칸이 문자길이보다 한 칸 작으면 최종 변수에 1 더함
                    if cnt_c == K - 1:
                        space += 1
                # 세로로 검사, 시작점은 열의 맨 처음 혹은 이전 행이 막힌 곳이어야 함
                if r == 0 or puzzle[r-1][c] == 0:
                    for nr in range(1, N-r):
                        if puzzle[r+nr][c]:
                            cnt_r += 1
                        else:
                            break
                    if cnt_r == K - 1:
                        space += 1


    print(f'#{tc} {space}')