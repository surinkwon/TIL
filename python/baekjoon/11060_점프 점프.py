'''
bfs
'''

import sys
from collections import deque

# 점프 횟수 찾는 함수
def findWay(s):
    q = deque()
    q.append(s)
    v = [-1] * N
    v[0] = 0
    
    while q:
        cn = q.popleft()

        for d in range(1, maze[cn] + 1):
            nn = cn + d
            if nn < N and v[nn] == -1:
                q.append(nn)
                v[nn] = v[cn] + 1
    
    return v[-1]

N = int(input())
maze = list(map(int, sys.stdin.readline().split()))

rlt = findWay(0)

print(rlt)