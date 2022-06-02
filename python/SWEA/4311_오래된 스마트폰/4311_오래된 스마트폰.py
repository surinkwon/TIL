import sys
# from collections import deque
# from itertools import product

sys.stdin = open('input.txt')

T = int(input())

# 터치할 수 있는 숫자로 만들 수 있는 n자리 숫자를 구하는 함수
def makeNums(i, n, num):
    global can_make_nums
    if i == n:
        can_make_nums.add(int(num))
    else:
        for j in range(len(nums)):
            makeNums(i+1, n, num+nums[j])

# 원하는 숫자를 만들 수 있는지, 터치 횟수는 몇 번인지 구하는 함수
def canMake():
    q = []
    # 숫자마다 터치 횟수가 달라지기 때문에 다익스트라처럼 해야 함
    v = [M+1] * 1000
    num_lst = list(can_make_nums)
    for i in range(len(num_lst)):
        q.append(num_lst[i])
        v[num_lst[i]] = len(str(num_lst[i]))

    qf = -1
    # 큐 리어는 큐의 가장 마지막 인덱스로 해야 한다! -1 안 붙이면 인덱스 에러
    qr = len(num_lst) - 1

    while qf != qr:
        qf += 1
        cn = q[qf]

        # 해당 숫자를 만들 수 있어도 터치 횟수를 넘어가면 -1 반환 / +1 해주는 이유는 =연산 터치 횟수
        if cn == want_num:
            if v[cn] + 1 > M:
                return -1
            return v[cn] + 1

        # 1: +, 2: -, 3: *, 4: /
        for d in range(len(opps)):
            if opps[d] == 1:
                for i in range(len(num_lst)):
                    nn = cn + num_lst[i]
                    # 각 숫자마다 터치 횟수가 다르기 때문에 이전에 먼저 해당 숫자를 만들었어도 최소 터치 횟수가 아닐 수 있음
                    if 0 <= nn <= 999 and v[nn] > v[cn] + len(str(num_lst[i])) + 1:
                        q.append(nn)
                        v[nn] = v[cn] + len(str(num_lst[i])) + 1
                        qr += 1

            elif opps[d] == 2:
                for i in range(len(num_lst)):
                    nn = cn - num_lst[i]
                    if 0 <= nn <= 999 and v[nn] > v[cn] + len(str(num_lst[i])) + 1:
                        q.append(nn)
                        v[nn] = v[cn] + len(str(num_lst[i])) + 1
                        qr += 1

            elif opps[d] == 3:
                for i in range(len(num_lst)):
                    nn = cn * num_lst[i]
                    if 0 <= nn <= 999 and v[nn] > v[cn] + len(str(num_lst[i])) + 1:
                        q.append(nn)
                        v[nn] = v[cn] + len(str(num_lst[i])) + 1
                        qr += 1

            else:
                for i in range(len(num_lst)):
                    if num_lst[i]:
                        nn = cn // num_lst[i]
                        if 0 <= nn <= 999 and v[nn] > v[cn] + len(str(num_lst[i])) + 1:
                            q.append(nn)
                            v[nn] = v[cn] + len(str(num_lst[i])) + 1
                            qr += 1

    return -1

for tc in range(1, T + 1):
    N, O, M = map(int, input().split())
    nums = list(input().split())
    opps = list(map(int, input().split()))
    want_num = int(input())
    rlt = -1

    can_make_nums = set()
    # 현재 숫자만으로 만들 수 있는 모든 수 확인
    for i in range(N):
        can_make_nums.add(int(nums[i]))
    makeNums(0, 2, '')
    makeNums(0, 3, '')

    # 현재 숫자만으로 만들 수 있으면
    if want_num in can_make_nums:
        rlt = len(str(want_num))

    else:
        # 연산으로 만들어야 한다면 구하기
        rlt = canMake()

    print(f'#{tc} {rlt}')

