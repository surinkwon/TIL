import sys

sys.stdin = open('input.txt')


def BFS(s):
    v = [0] * 101
    q = [0] * 101
    f = r = -1
    r += 1
    q[r] = s
    v[s] = 1

    while f != r:
        f += 1
        cn = q[f]

        '''
        이렇게 조건 걸어주는 것을 먼저 생각하자
        if v[max_num] <= v[cn] and max_num < cn:
            max_num = cn
        '''

        for i in range(1, len(phone_book[cn])):
            if phone_book[cn][i] and v[i] == 0:
                r += 1
                q[r] = i
                v[i] = v[cn] + 1
    
    # 이렇게 다 계산하고 마지막에 큰 걸 찾는 게 아니라 큐 연산하면서 조건 찾는 것을 먼저 생각해보기
    max_v = v[q[r]]
    max_num = q[r]

    for j in range(r - 1, -1, -1):
        if v[q[j]] < max_v:
            break
        elif v[q[j]] == max_v and max_num < q[j]:
            max_num = q[j]

    return max_num


for tc in range(1, 11):
    N, start = map(int, input().split())
    phone_data = list(map(int, input().split()))
    phone_book = [[0] * 101 for _ in range(101)]

    for i in range(0, len(phone_data), 2):
        phone_book[phone_data[i]][phone_data[i+1]] = 1

    rlt = BFS(start)

    print(f'#{tc} {rlt}')