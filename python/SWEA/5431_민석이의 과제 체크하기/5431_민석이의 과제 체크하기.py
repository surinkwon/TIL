import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    dat = [0] * (N + 1)
    ns = [] # 과제 안 낸 사람 번호 담을 리스트

    for i in range(len(submit)):
        dat[submit[i]] = 1

    for i in range(1, len(dat)):
        if dat[i] == 0:
            ns.append(i)

    print(f'#{tc} {" ".join(str(i) for i in ns)}')

