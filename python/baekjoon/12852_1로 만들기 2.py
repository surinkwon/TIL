'''
bfs
'''

from collections import deque

def makeOne(n):
    q = deque()
    q.append([n, [n]])
    v = [0] * (n + 1)
    v[n] = 1

    while q:
        cn, clst = q.popleft()

        if cn == 1:
            return v[cn] - 1, clst
        
        # 몫하고 나머지 구하는거 헷갈리지 말고 정신 차리고 조건 지정하기
        if cn // 3 > 0 and cn % 3 == 0 and v[cn//3] == 0:
            q.append([cn//3, clst + [cn//3]])
            v[cn//3] = v[cn] + 1
        
        if cn // 2 > 0 and cn % 2 == 0 and v[cn//2] == 0:
            q.append([cn//2, clst + [cn//2]])
            v[cn//2] = v[cn] + 1
        
        if cn - 1 > 0 and v[cn-1] == 0:
            q.append([cn-1, clst + [cn-1]])
            v[cn-1] = v[cn] + 1
    

N = int(input())

rlt_num, rlt_lst = makeOne(N)

print(rlt_num)

for i in range(len(rlt_lst)):
    print(rlt_lst[i], end=' ')