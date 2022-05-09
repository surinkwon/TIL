'''
A -> B
bfs
일반 v배열 만들어서 풀면 메모리초과 난다. B가 최대 10^9승이기 때문일 것
따라서 다른 방법이 필요하다. 
질문 검색에서 조금 참고해서 풀었다...

큐에 넣을 때는 꼭 숫자 하나만 넣을 필요가 없다는 것을 기억하자!!!
어떤 자료형이든 넣을 수 있고 그걸 이용할 수 있으면 된다.
'''
from collections import deque

def bfs():
    global n_dict
    
    q = deque()
    q.append((A, 1))

    while q:
        cn, cnt = q.popleft()

        if cn == B:
            return cnt
        
        if cn * 2 <= B and n_dict.get(cn*2) == None:
            q.append((cn*2, cnt + 1))
            n_dict[cn*2] = 1
        
        tmp = str(cn)+'1'
        if len(tmp) <= 10:
            tmp = int(tmp)
            if tmp <= B and n_dict.get(tmp) == None:
                q.append((tmp, cnt + 1))
                n_dict[tmp] = 1
    
    return -1


A, B = map(int, input().split())
n_dict = {}
rlt = bfs()
print(rlt)