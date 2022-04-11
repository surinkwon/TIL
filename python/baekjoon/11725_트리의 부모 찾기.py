'''
리스트에 부모 번호를 담는 방식으로 구현
'''
import sys
from collections import deque

def bfs(s):
    global parents
    q = deque()
    q.append(s)

    while q:
        cn = q.popleft()

        for d in range(len(tree[cn])):
            if parents[tree[cn][d]] == 0:
                q.append(tree[cn][d])
                parents[tree[cn][d]] = cn


N = int(input())
tree = [set() for _ in range(N + 1)]
parents = [0] * (N + 1)
parents[1] = 1


for i in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    if node2 not in tree[node1]:
        tree[node1].add(node2)
    if node1 not in tree[node2]:
        tree[node2].add(node1)

for i in range(len(tree)):
    tree[i] = list(tree[i])

bfs(1)

for i in range(2, len(parents)):
    print(parents[i])






