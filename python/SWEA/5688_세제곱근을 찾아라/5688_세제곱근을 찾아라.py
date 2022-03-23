import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    start = 1
    end = N
    rlt = -1

    # 1부터 제곱 검사를 하는데 end는 N을 start로 나눈 값이므로
    # start * end를 하면 N이 나옴 따라서 end가 start의 제곱과 같으면 start가 세제곱근이 됨
    # 조건 지정 유의하기 이걸 start < end라고 하면 시간초과
    # start ** 2 < end하면 답이 제대로 나오지 않음
    while start ** 2 <= end: 
        if start ** 2 == end:
            rlt = start
            break
        else:
            start += 1
            end = N // start

    print(f'#{tc} {rlt}')

