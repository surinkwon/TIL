import sys

N, M = map(int, sys.stdin.readline().split())
t = 0

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for _ in range(N):
    t += sum(matrix(_))

K = int(input())

for t in range(K):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    total = t
    for i in range(r1):
        for j in range(c1):
            total -= matrix[i][j]
    
    for i in range(r2 + 1, len(matrix)):
        for j in range(c2 + 1, len(matrix[i])):
            total -= matrix[i][j]
    
    print(total)
