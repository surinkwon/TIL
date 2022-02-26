import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_numbers = list(map(int, input().split()))
    M_numbers = list(map(int, input().split()))
    max_sum = -987654321

    # 더 적은 수를 가진 배열을 찾음
    if len(N_numbers) > len(M_numbers):
        for i in range(len(N_numbers) - len(M_numbers) + 1):
            s = 0
            for j in range(len(M_numbers)):
                s += N_numbers[i + j] * M_numbers[j]

            if max_sum < s:
                max_sum = s
    else:
        for i in range(len(M_numbers) - len(N_numbers) + 1):
            s = 0
            for j in range(len(N_numbers)):
                s += M_numbers[i + j] * N_numbers[j]

            if max_sum < s:
                max_sum = s

    print(f'#{tc} {max_sum}')

