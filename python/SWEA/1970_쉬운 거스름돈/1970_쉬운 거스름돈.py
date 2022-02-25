import sys

sys.stdin = open('input.txt')

T = int(input())

# 거스름돈 종류
dat = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T + 1):
    change = int(input())
    change_num = [0] * len(dat)

    i = 0
    while i < len(dat):
        if change >= dat[i]:
            change_num[i] += 1
            change -= dat[i]
        else:
            i += 1

    print(f'#{tc}')
    print(' '.join([str(x) for x in change_num]))

