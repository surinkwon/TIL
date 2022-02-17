import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    # 날짜를 뒤에서부터 읽기 위해 역순으로 바꿔서 저장
    n_lst = list(map(int, input().split()))[::-1]
    profit = 0
    i = j = 0
    
    # 뒤쪽 날짜의 가격보다 앞쪽 날짜의 가격이 작으면 이윤에 차이만큼 더함
    while j < len(n_lst):
        m = n_lst[i]
        if n_lst[j] < m:
            profit += m - n_lst[j]
        
        # 가격이 같거나 앞쪽 날짜 가격이 더 크면 해당 값을 최댓값으로 정함
        else: 
            i = j
        j += 1

    print(f'#{tc} {profit}')

