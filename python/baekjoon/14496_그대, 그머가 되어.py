from collections import deque

# 최소 변환 횟수를 찾는 함수
def findMinChange(s):
    q = deque()
    v = [0] * (N + 1)
    v[s] = 1
    q.append(s)

    while q:
        cn = q.popleft()

        # 가장 먼저 목표 단어에 도착하는 횟수가 최소 횟수
        if cn == B:
            return v[cn] - 1

        for d in range(len(words[cn])):
            nn = words[cn][d]

            if not v[nn]:
                q.append(nn)
                v[nn] = v[cn] + 1

    return -1

A, B = map(int, input().split())

N, M = map(int, input().split())
words = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    words[s].append(e)
    words[e].append(s)

rlt = findMinChange(A)

print(rlt)