'''
다익스트라
'''
from collections import deque

def findItemNum(start):
    q = deque()
    v = [99999999] * (n + 1)
    v[start] = 0
    q.append((start, 0))

    rlt = items[start]

    while q:
        cn, cd = q.popleft()

        for d in range(len(road[cn])):
            nn = road[cn][d]
            nd = cd + distance[cn][nn]

            # 아이템 개수 측정을 위해 이전에 방문할 수 있었던 곳인지 아닌지 확인 필요
            # 이전보다 더 적은 거리로 갈 수 있는 곳이면 거리 갱신 필요, 거기에서 다른 곳으로 갈 수도 있기 때문에
            if nd <= m and v[nn] > nd:
                if v[nn] == 99999999:
                    rlt += items[nn]
                    q.append((nn, nd))
                    v[nn] = nd
                else:
                    q.append((nn, nd))
                    v[nn] = nd

    return rlt


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
road = [[] for _ in range(n + 1)]
distance = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    s, e, d = map(int, input().split())
    road[s].append(e)
    road[e].append(s)
    distance[s][e] = distance[e][s] = d

max_item_num = 0

for i in range(1, n + 1):
    tmp = findItemNum(i)
    max_item_num = max(max_item_num, tmp)

print(max_item_num)