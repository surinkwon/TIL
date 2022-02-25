import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    test = list(map(int, input().split()))
    dat = [0] * 101
    sorted_test = [0] * len(test)
    rlt = 0

    # 카운팅 소트
    for i in range(len(test)):
        dat[test[i]] += 1

    for i in range(1, len(dat)):
        dat[i] += dat[i - 1]

    for i in range(len(test)):
        dat[test[i]] -= 1
        sorted_test[dat[test[i]]] = test[i]

    for idx in range(len(sorted_test) - 1, len(sorted_test) - K - 1, -1):
        rlt += sorted_test[idx]

    print(f'#{tc} {rlt}')

