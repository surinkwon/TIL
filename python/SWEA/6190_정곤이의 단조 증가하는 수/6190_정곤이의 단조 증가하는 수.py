import sys

sys.stdin = open('input.txt')

T = int(input())


# 단조 증가 수 구하는 함수
def isMono(num):
    # 숫자를 뒤에서부터 비교함
    after = num % 10 # after가 자릿수가 더 작은 것
    num //= 10

    while num != 0:
        before = num % 10 # before는 자릿수가 더 큰 것

        if after < before:
            return 0
        after = before
        num //= 10

    return 1


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_mono = 0

    if N == 1: # 수가 한 개만 들어왔을 땐 그것이 가장 큰 단조 증가 수
        max_mono = numbers[0]
    else:
        # 두 원소를 곱하므로 이중포문
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                mul = numbers[i] * numbers[j]
                if isMono(mul):
                    if max_mono < mul:
                        max_mono = mul

    if max_mono == 0:
        max_mono = -1

    print(f'#{tc} {max_mono}')

