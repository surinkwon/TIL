'''
숨바꼭질하고 비슷하게 풀면 됨
bfs
완탐
'''
from collections import deque

def howManyButton(s):
    floor = [0] * (F + 1)
    q = deque()
    q.append(s)
    floor[s] = 1

    while q:
        cf = q.popleft()

        # 층에 도달했다는 것은 맨 처음으로 그 장소에 갔다는 것이므로 누른 버튼 수 반환
        # 맨 처음 층은 누르지 않았는데 1로 설정했으므로 1을 빼줌
        if cf == G:
            return floor[G] - 1
        
        nf = cf + U
        if nf < len(floor) and floor[nf] == 0:
            floor[nf] = floor[cf] + 1
            q.append(nf)
        
        nf = cf - D
        if nf > 0 and floor[nf] == 0:
            floor[nf] = floor[cf] + 1
            q.append(nf)
    
    # 다 눌러봤는데 못가면 계단으로 가라
    return 'use the stairs'


F, S, G, U, D = map(int, input().split())

rlt = howManyButton(S)

print(rlt)
