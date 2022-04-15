'''
각 경로마다 가는 길이 있으면 bfs돌기
만약 이미 갔던 길이라면 그냥 지나감
'''
import sys
from collections import deque

def bfs(r, c):
    q = deque()
    q.append(c)

    while q:
        cc = q.popleft()

        for d in range(N):
            if graph[cc][d] and route[r][d] == '0':
                q.append(d)
                route[r][d] = '1'

N = int(input())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
route = [['0'] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] and route[i][j] == '0':
            route[i][j] = '1'
            bfs(i, j)

for i in range(N):
    print(' '.join(route[i]))


