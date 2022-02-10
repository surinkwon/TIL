import sys

sys.stdin = open('input.txt')

T = 10

# 2차원 배열 가로, 세로 바꿔서 재배열
def rotation(lst, r, c): # 배열, 배열의 행 수, 배열의 열 수
    ro_lst = [[0]*r for _ in range(c)] # 입력받은 배열의 행 수만큼 열 생성, 열 수만큼 행 생성
    
    for i in range(c):
        for j in range(r):
            ro_lst[i][j] = lst[j][i]
    
    return ro_lst

# 리스트 원소들의 합을 구하는 함수
def sum_lst(lst):
    total = 0
    for i in lst:
        total += i
    
    return total

# 리스트의 대각선(왼쪽부터) 원소의 합을 구하는 함수(문제처럼 행, 열 개수가 같을 때)
def dia_sum_left(lst):
    total = i = j = 0
    while i < len(lst):
        total += lst[i][j]
        i += 1
        j += 1
    
    return total

# 리스트의 대각선(오른쪽부터) 원소의 합을 구하는 함수
def dia_sum_right(lst):
    total = i = 0
    j = len(lst) - 1
    while i < len(lst):
        total += lst[i][j]
        i += 1
        j -= 1

    return total

# 최댓값 함수
def max_lst_sum(lst):
    max_value = lst[0]
    for i in lst:
        if max_value < i:
            max_value = i
    
    return max_value

for tc in range(1, T + 1):
    test = int(input())
    # 입력값 2차원 배열
    num_lst = [0] * 100
    for i in range(len(num_lst)):
        num_lst[i] = list(map(int, input().split()))

    max_sum = 0
    sums = [] # 각 행, 열의 합을 저장할 리스트

    # 2차원 배열을 재정렬 한 배열
    rot_num_lst = rotation(num_lst, 100, 100)
    
    # 원 배열과 재정렬 한 배열의 행들의 합을 저장
    for idx in range(100):
        sums.extend([sum_lst(num_lst[idx]), sum_lst(rot_num_lst[idx])])
    
    max_sum = max_lst_sum(sums) # 합들의 최댓값
    # (왼)대각선 합, (오른)대각선 합, 합 최댓값 중 최댓값을 구함
    rlt = max_lst_sum([dia_sum_left(num_lst), dia_sum_right(num_lst), max_sum])

    print(f'#{tc} {rlt}')

