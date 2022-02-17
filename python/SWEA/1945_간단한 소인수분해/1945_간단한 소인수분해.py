import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())

    # DAT(소인수 분해에 이용되는 소수가 정해져 있으므로 사용)
    dat = [2, 3, 5, 7, 11]
    cnt = [0] * len(dat)

    # 입력받은 값이 DAT의 해당 값으로 나눠지면 카운트
    i = 0
    while N != 1:
        if N % dat[i]:
            i += 1
        else:
            N //= dat[i]
            cnt[i] += 1

    print(f'#{tc} {" ".join([str(x) for x in cnt])}')

