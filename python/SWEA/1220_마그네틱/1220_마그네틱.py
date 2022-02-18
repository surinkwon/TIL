import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    
    # N극과 S극이 번갈아서 교착상태로 세어줌
    for j in range(N):
        n = s = 0
        for i in range(N):
            if table[i][j] == 1:
                n += 1
            else:
                if table[i][j] == 2 and n >= 1:
                    n = 0 # n값을 초기화해주지 않으면 이후에 n극 2개, s극 두개로 나올 때도 2번으로 세어짐
                    total += 1

    print(f'#{tc} {total}')

