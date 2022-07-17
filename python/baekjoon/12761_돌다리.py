'''
그래프이론
범위는 문제에서 주어진 대로 정할 것
bfs로 풀이
'''
from collections import deque

def goToJumi():
    q = deque()
    q.append(N)
    v = [0] * 100001
    v[N] = 1

    while q:
        cn = q.popleft()

        if cn == M:
            return v[cn] - 1

        can_move = [cn + 1, cn - 1, cn + A, cn - A, cn + B, cn - B, cn * A, cn * B]

        for d in range(8):
            nn = can_move[d]
            if 0 <= nn < 100001 and v[nn] == 0:
                q.append(nn)
                v[nn] = v[cn] + 1

    return v[M] - 1


A, B, N, M = map(int, input().split())

answer = goToJumi()

print(answer)