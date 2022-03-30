'''
방문 배열을 전역변수로 두고 방문을 체크한 다음 방문한 곳은 다시 방문하지 않음
그럼 BFS를 한 번 돌 때마다 하나의 연결요소를 방문 가능
파이썬으로 했는데 계속 시간초과나서 pypy로 돌리니까 통과함...
'''

from collections import deque


def bfs(s):
    global v
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        for d in connect[c]:
            if v[d] == 0:
                q.append(d)
                v[d] = 1
    
    return 1

N, M = map(int, input().split())
connect = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    connect[s].append(e)
    connect[e].append(s)

v = [0] * (N+1)
cnt = 0

for i in range(1, N+1):
    if v[i] == 0:
        cnt += bfs(i)

print(cnt)