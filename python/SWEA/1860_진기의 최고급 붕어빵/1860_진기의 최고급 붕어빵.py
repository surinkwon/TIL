import sys

sys.stdin = open('input.txt')

T = int(input())
# 버블소트 함수
def bubble(lst):
    for i in range(len(lst), 0, -1):
        for j in range(1, i):
            if lst[j] < lst[j - 1]:
                tem = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = tem
    return lst

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    can = 'Possible'

    # 손님 리스트 정렬
    # 인덱스를 여태까지 도착한 손님 수로 사용하기 위해 앞에 0을 하나 붙여줌
    lst = [0] + bubble(lst)

    for i in range(1, N+1):
        # 손님이 도착한 시간에서 붕어빵을 K개 만드는 시간을 나눈 몫은
        # 해당 시간까지 붕어빵을 총 몇 '번' 만들 수 있는지를 나타냄
        if (lst[i] // M) * K - i < 0:
            can = 'Impossible'

    print(f'#{tc} {can}')

