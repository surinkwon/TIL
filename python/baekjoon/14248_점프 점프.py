'''
bfs
'''

from collections import deque

def canGo(s):
    q = deque()
    q.append(s)
    v = [0] * (N + 1)
    v[s] = 1
    cnt = 1

    while q:
        cr = q.popleft()

        if cr + rocks[cr] < N + 1 and v[cr + rocks[cr]] == 0:
            q.append(cr+rocks[cr])
            v[cr + rocks[cr]] = 1
            cnt += 1
        
        if cr - rocks[cr] > 0 and v[cr - rocks[cr]] == 0:
            q.append(cr-rocks[cr])
            v[cr - rocks[cr]] = 1
            cnt += 1
    
    return cnt


N = int(input())
rocks = [0] + list(map(int, input().split()))
start = int(input())

rlt = canGo(start)

print(rlt)