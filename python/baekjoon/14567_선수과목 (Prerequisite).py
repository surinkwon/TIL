'''
위상정렬 + bfs 살짝 곁들임
'''
from collections import deque
import sys

def howManySemester():
    v = [0] * (N + 1)
    q = deque()
    for s in range(1,len(pre)):
        if pre[s] == 0:
            v[s] = 1
            q.append(s)
    
    while q:
        cs = q.popleft()

        for d in range(len(subjects[cs])):
            pre[subjects[cs][d]] -= 1
            if pre[subjects[cs][d]] == 0:
                v[subjects[cs][d]] = v[cs] + 1
                q.append(subjects[cs][d])

    return v


N, M = map(int, input().split())
pre = [0] * (N + 1)
subjects = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, sys.stdin.readline().split())

    subjects[p].append(c)
    pre[c] += 1

rlt = howManySemester()

print(' '.join([str(rlt[i]) for i in range(1, len(rlt))]))
