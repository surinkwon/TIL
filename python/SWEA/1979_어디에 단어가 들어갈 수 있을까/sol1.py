import sys

sys.stdin = open('input.txt')

T = int(input())
def isSpace(lst):
    s = 0
    for c in range(len(lst)):
        cnt = 0
        if lst[c] == 1:
            # 가로로 검사, 시작점은 행의 맨 처음 혹은 이전 열이 막힌 곳이어야 함
            if c == 0 or lst[c - 1] == 0:
                for nc in range(len(lst) - c):  # 지금 열에서 마지막 열까지
                    if lst[c + nc]:  # 빈 공간을 만나면 + 1
                        cnt += 1
                    else:
                        break  # 막혀있으면 빠져나옴

                if cnt == K:
                    s += 1
    return s

for tc in range(1, T + 1):
    # 퍼즐 크기, 단어 길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    space = 0
    # 전치
    puzzle_t = list(zip(*puzzle))

    for i in range(N):
        space += isSpace(puzzle[i]) + isSpace(puzzle_t[i])

    print(f'#{tc} {space}')

