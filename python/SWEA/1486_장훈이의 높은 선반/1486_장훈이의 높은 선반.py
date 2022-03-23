import sys

sys.stdin = open('input.txt')

T = int(input())


# 부분조합 함수 잘 기억해두자
def subSet(i, lst, tall_lst, s, sh):
    global d
    
    # 백 트래킹 부분
    if s == sh:
        d = 0
        return

    elif s > sh:
        if d > abs(sh - s):
            d = abs(sh - s)
        return

    elif i == len(lst):
        return
    
    # 부분집합에 포함되는 원소인지 아닌지를 파악하기 위해서 lst를 두고
    # 해당 원소가 포함되지 않을 때를 설정하고 함수 호출
    # 해당 원소가 포함되었을 때를 설정하고 함수 호출
    else:
        lst[i] = 0
        subSet(i + 1, lst, tall_lst, s, sh)
        lst[i] = 1
        subSet(i+1, lst, tall_lst, s+tall_lst[i], sh)


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    d = 987654321
    bit = [0] * N
    subSet(0, bit, clerk, 0, B)

    print(f'#{tc} {d}')

