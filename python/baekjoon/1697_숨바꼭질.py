from collections import deque


def BFS(start, goal):
    v = [0] * 100001
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        cn = q.popleft()

        if cn == goal:
            return v[cn] - 1
        
        for i in range(3):
            if i == 0:
                nn = cn + 1
            elif i == 1:
                nn = cn - 1
            else:
                nn = cn * 2

            # 조건 지정 잘 하자!!!! 범위 지정 중요!!
            if 0 <= nn <= 100000 and v[nn] == 0:
                q.append(nn)
                v[nn] = v[cn] + 1

N, M = map(int, input().split())
rlt = BFS(N, M)
print(rlt)