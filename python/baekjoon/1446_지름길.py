'''
다익스트라
문제에서 시작위치가 도착위치가 작다는 조건은 시작위치가 최종 도착해야하는 지점보다 작다는 의미가 아니다
'''

from collections import deque

# 지름길 찾는 함수
def goFast():
    v = [99999999] * (D + 1)
    q = deque()
    q.append(0)
    v[0] = 0

    while q:
        cn = q.popleft()

        for idx in range(len(bypass[cn])):
            end, d = bypass[cn][idx]
            if end < D + 1 and v[end] > v[cn] + d:
                q.append(end)
                v[end] = v[cn] + d

        if cn < D and v[cn + 1] > v[cn] + 1:
            q.append(cn+1)
            v[cn + 1] = v[cn] + 1

    return v[D]

N, D = map(int, input().split())

bypass = [[] for _ in range(D + 1)]

# 우회로 등록
for _ in range(N):
    start, end, d = map(int, input().split())

    if start < D:
        bypass[start].append((end, d))

rlt = goFast()

print(rlt)