import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

# dat
dat = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T + 1):
    other_num_data = input() # 테스트 케이스 번호, 들어오는 번호 수
    other_num_lst = list(input().split()) # 다른 행성 숫자
    cnt = [0] * len(dat) # dat를 활용하기 위한 카운트 리스트

    # 다른 행성 숫자 리스트가 dat의 값과 같다면 카운트 + 1
    for i in range(len(other_num_lst)):
        for j in range(len(dat)):
            if other_num_lst[i] == dat[j]:
                cnt[j] += 1

    print(f'#{tc}')
    
    # zro부터 있는 수만큼 출력 
    for k in range(len(cnt)):
        if cnt[k] >= 1:
            print(f'{dat[k]} '*cnt[k], end=' ')
    print()
