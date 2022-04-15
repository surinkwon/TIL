'''
위상정렬
indegree 배열을 만들어주고 bfs 돌리듯 돌리면 됨

위상정렬은 방향이 있고 circle이 없는 그래프에서 할 수 있는데
indegree에는 나에게로 들어오는 화살표(내가 몇 개를 거쳐야 만들어질 수 있는지)
나에게로 몇개의 방향성 있는 간선이 이어지는지 개수를 세서 넣어주면 됨(내 차례가 되기 위한 조건)

indegree가 0이면 내 차례가 될 때까지 아무런 필요한 조건이 없다는 것이므로 q에 넣어줌
'''
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
students = [[] for _ in range(N + 1)]

for _ in range(M):
    s1, s2 = map(int, input().split())
    students[s1].append(s2)

    indegree[s2] += 1

q = deque()

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

while q:
    ci = q.popleft()
    print(ci, end=' ')

    for d in range(len(students[ci])):
        indegree[students[ci][d]] -= 1
        if indegree[students[ci][d]] == 0:
            q.append(students[ci][d])
