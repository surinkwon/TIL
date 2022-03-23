import sys
from collections import deque

sys.stdin = open('input.txt')

T = 10


def calling(ph, s):
    # bfs 활용
    v = [0] * 101
    q = deque()
    v[s] = 1
    q.append(s)
    max_num = s

    while q:
        point = q.popleft()
        # 조건을 걸어주는 곳, 마지막 전화건 사람 중 가장 번호가 큰 것 저장
        if v[max_num] < v[point] or v[max_num] == v[point] and max_num < point:
            max_num = point

        if ph[point]:
            for j in range(len(ph[point])):
                if v[ph[point][j]] == 0:
                    q.append(ph[point][j])
                    v[ph[point][j]] = v[point] + 1

    return max_num


for tc in range(1, T + 1):
    con, start = map(int, input().split())
    nums = list(map(int, input().split()))
    phones = [[] for _ in range(101)]

    # 비상 연락망 구성
    for i in range(0, len(nums), 2):
        p1, p2 = nums[i], nums[i+1]
        if p2 not in phones[p1]:
            phones[p1].append(p2)

    # 연락 돌리기
    max_p = calling(phones, start)

    print(f'#{tc} {max_p}')

