import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(input().split())
    rlt = [0] * N
    
    # 카드 리스트를 반으로 나눠줌
    if N % 2:
        f = lst[:N // 2 + 1]
        s = lst[N // 2 + 1:]
    else:
        f = lst[:N // 2]
        s = lst[N // 2:]

    i = j = 0
    # 반으로 나눈 리스트를 번갈아가며 결과에 넣어줌
    while i < N:
        if i % 2:
            rlt[i] = s[j]
            j += 1
        else:
            rlt[i] = f[j]
        i += 1

    print(f'#{tc} {" ".join(rlt)}')

