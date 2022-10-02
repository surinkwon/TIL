'''
python은 시간초과
bfs로 풀이
'''

from collections import deque

def calPreWork(s):
    q = deque()
    v = [0] * (N + 1)
    v[s] = 1
    q.append(s)
    cnt = 0

    while q:
        cw = q.popleft()

        for d in range(len(pre_work_info[cw])):
            pre_w = pre_work_info[cw][d]

            if not v[pre_w]:
                v[pre_w] = 1
                q.append(pre_w)
                cnt += 1
    
    return cnt

N, M = map(int, input().split())
pre_work_info = [[] for _ in range(N + 1)]

for _ in range(M):
    pre, post = map(int, input().split())

    pre_work_info[post].append(pre)

X = int(input())

rlt = calPreWork(X)

print(rlt)