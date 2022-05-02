from collections import deque
import sys


def findNum(s):
    v = [0] * (N + 1)
    q = deque()
    q.append(s)
    v[s] = 1
    rlt = 0
    cnt = N - 1

    while q:
        cn = q.popleft()

        if cnt == 0:
            return rlt
        
        for d in range(len(connection[cn])):
            nn = connection[cn][d]
            if v[nn] == 0:
                cnt -= 1
                v[nn] = v[cn] + 1
                rlt += v[cn]
                q.append(nn)
    
    return rlt


N, M = map(int, input().split())
connection = [set() for _ in range(N + 1)]
min_num = 99999999
answer = 0

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    connection[data[0]].add(data[1])
    connection[data[1]].add(data[0])

for i in range(1, N + 1):
    connection[i] = list(connection[i])

for i in range(1, N + 1):
    tmp = findNum(i)
    if min_num > tmp:
        min_num = tmp
        answer = i

print(answer)

