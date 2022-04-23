'''
다익스트라..?

도달한 경로까지 거쳐온 점의 수가 같거나 더 적을 때만 큐에 추가 
'''
from collections import deque

def minWay():
    v = [99999999] * 1000001
    cnt = 0
    q =  deque()
    q.append(N)
    v[N] = 1

    while q:
        cn = q.popleft()

        # 이미 최소 경로의 수를 넘었느면 그 이상은 탐색하지 않음
        # 이거 안 넣으면 시간 너무 오래 걸림
        if v[cn] > v[K]:
            continue

        if cn == K:
            cnt += 1
            mt = v[cn]

        if 0 <= cn + 1 < len(v) and v[cn + 1] >= v[cn] + 1:
            q.append(cn+1)
            v[cn + 1] = v[cn] + 1
        
        if 0 <= cn - 1 < len(v) and v[cn - 1] >= v[cn] + 1:
            q.append(cn-1)
            v[cn - 1] = v[cn] + 1

        if 0 <= cn * 2 < len(v) and v[cn * 2] >= v[cn] + 1:
            q.append(cn*2)
            v[cn * 2] = v[cn] + 1

    return mt, cnt


N, K = map(int, input().split())
min_time, count = minWay()
print(min_time-1)
print(count)