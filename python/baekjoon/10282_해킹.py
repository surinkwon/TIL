'''
다익스트라 

처음에는 의존성을 나타내는 인접 리스트를 만들고 
의존성에 따른 감염 시간을 담는 인접 행렬을 따로 만들어서 돌렸더니 메모리 초과가 나왔다.
n이 10000까지 될 수 있어서 그런 것 같았다. 그래서 인접 리스트를 저장할 때 시간도 함께 저장하도록
고치니 통과되었다.

메모리와 시간 둘다 초과나지 않도록 인접 리스트, 행렬을 만들때 고려를 잘 해야겠다. 
(이번 문제에서는 같은 의존성이 두 번 이상 존재하지 않아서 쉽게 구현할 수 있었는데
같은 의존성이 나오면 어떻게 저장할 지도 생각해 보는 게 좋겠다.)
'''
from collections import deque
import sys

def infect(s):
    q = deque()
    q.append((s, 0))
    v = [99999999] * (n + 1)
    v[s] = 0
    last_time = 0
    infected = 0

    while q:
        cc, ct = q.popleft()

        for d in range(len(dependency[cc])):
            nc = dependency[cc][d][0]
            if v[nc] > ct + dependency[cc][d][1]:
                q.append((nc, ct + dependency[cc][d][1]))
                v[nc] = ct + dependency[cc][d][1]
    
    for c in range(1, n + 1):
        if v[c] != 99999999:
            if v[c] > last_time:
                last_time = v[c]
            infected += 1
    
    return infected, last_time

T = int(input())

for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())
    dependency = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        dependency[b].append([a, s])
    
    total_infected, total_time = infect(c)
    print(total_infected, total_time)



