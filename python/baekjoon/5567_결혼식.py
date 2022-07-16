'''
그래프
bfs로 해결
상근이의 친구를 q에 넣고 해당 친구의 친구들만 세기
'''
from collections import deque
import sys

def invite(s):
    q = deque()
    v = [0] * (N + 1)
    rlt = 0
    v[1] = 1

    for i in range(len(mate[s])):
        q.append(mate[s][i])
        v[mate[s][i]] = 1
        rlt += 1
    
    while q:
        cn = q.popleft()

        for d in range(len(mate[cn])):
            if v[mate[cn][d]] == 0:
                v[mate[cn][d]] = 1
                rlt += 1
    
    return rlt


N = int(input())
M = int(input())
mate = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mate[a].append(b)
    mate[b].append(a)

answer = invite(1)

print(answer)