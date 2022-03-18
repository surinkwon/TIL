from collections import deque

def BFS(start):
    v = [0] * (N+1)
    q = deque()
    v[start] = 1
    q.append(start)
    birus = 0

    while q:
        com = q.popleft()
        birus += 1

        for c in range(len(coms[com])):
            new_com = coms[com][c]
            if v[new_com] == 0:
                q.append(new_com)
                v[new_com] = 1
    
    return birus - 1 # 첫번째 컴퓨터 제외


N = int(input())
M = int(input())
coms = [[] for _ in range(N+1)]

# 그래프 구성
for _ in range(M):
    s, e = map(int, input().split())

    if e not in coms[s]:
        coms[s].append(e)
    if s not in coms[e]:
        coms[e].append(s)

rlt = BFS(1)
print(rlt)
