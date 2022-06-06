'''
위상 정렬
'''

import sys
from collections import deque

# 문제 순서 구하는 함수
def order():
    rlt = []
    q = deque()
    can = []
    # 바로 풀 수 있는 문제를 배열에 추가
    for i in range(1, N + 1):
        if indegree[i] == 0:
            can.append(i)
    
    # 바로 풀 수 있는 문제 중 가장 번호가 작은 문제를 큐에 추가
    q.append(can[0])
    rlt.append(can[0])
    can.pop(0)
    
    while q:
        cn = q.popleft()

        # 해당 문제를 푼 후 풀 수 있는 다른 문제들에 대한 필요 문제 개수를 줄여줌
        for d in range(len(connect[cn])):
            indegree[connect[cn][d]] -= 1

            # 만약 그 문제를 이제 풀 수 있으면 풀 수 있는 문제 리스트에 추가
            if indegree[connect[cn][d]] == 0:
                can.append(connect[cn][d])
        
        # 풀 수 있는 문제 리스트 중 가장 번호가 작은 문제를 큐에 추가
        if can:
            can.sort()
            q.append(can[0])
            rlt.append(can[0])
            can.pop(0)

    return rlt


N, M = map(int, input().split())

# 해당 문제를 풀기 전 남은 문제 개수
indegree = [0] * (N + 1)

# 해당 문제를 푼 뒤 풀 수 있는 문제들
connect = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connect[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    connect[i].sort()

rlt = order()

for i in range(len(rlt)):
    print(rlt[i], end=' ')