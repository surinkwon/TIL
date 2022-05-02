'''
0초일 때가 조건에 껴 있기 때문에 다익스트라로 풀어야 함
'''
from collections import deque

def findWay():
    q = deque()
    v = [99999999] * 100001
    q.append(N)
    v[N] = 1

    while q:
        cn = q.popleft()

        if cn == K:
            return v[K] - 1
        
        nn = cn * 2
        if 0 <= nn <= 100000 and v[nn] > v[cn]:
            q.append(nn)
            v[nn] = v[cn]

        nn = cn + 1
        if 0 <= nn <= 100000 and v[nn] > v[cn] + 1:
            q.append(nn)
            v[nn] = v[cn] + 1

        nn = cn - 1
        if 0 <= nn <= 100000 and v[nn] > v[cn] + 1:
            q.append(nn)
            v[nn] = v[cn] + 1


N, K = map(int, input().split())

rlt = findWay()

print(rlt)