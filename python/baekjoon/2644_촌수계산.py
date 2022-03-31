'''
bfs로 가는 길목이 촌수가 됨
근데 bfs로는 나부터 1촌으로 시작하므로 마지막에 하나를 빼줘야 함
'''
from collections import deque

def findKinship(s, e):
    v = [0] * (N + 1)
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        f = q.popleft()

        if f == e:
            return v[f] - 1
        
        for i in range(1, len(family[f])):
            if family[f][i] and v[i] == 0:
                q.append(i)
                v[i] = v[f] + 1
    
    return -1



N = int(input())
start, end = map(int, input().split())
M = int(input())
family = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split())
    family[p][c] = 1
    family[c][p] = 1

rlt = findKinship(start, end)

print(rlt)