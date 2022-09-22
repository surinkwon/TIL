'''
다익스트라
python으로 하면 시간초과, pypy로 하면 통과
'''

from collections import deque

def findWay(s):
    q = deque()
    INF = 99999999
    v = [INF] * (N + 1)
    v[s] = 0
    q.append(s)

    while q:
        cn = q.popleft()

        for d in range(len(road[cn])):
            nn = road[cn][d]
            if v[nn] > v[cn] + 1:
                q.append(nn)
                v[nn] = v[cn] + 1
    
    return v


N, M, K, X = map(int, input().split())
cnt = 0
road = [set() for _ in range(N + 1)]

## 도로 중복입력을 막고자 셋에 등록
for _ in range(M):
    s, e = map(int, input().split())
    road[s].add(e)

for i in range(N + 1):
    road[i] = list(road[i])

distances = findWay(X)

for i in range(N + 1):
    if distances[i] == K:
        cnt += 1
        print(i)

if not cnt:
    print(-1)