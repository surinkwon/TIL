N = int(input())
y = [0] * N
x = [0] * N
total = 0

for i in range(N):
    x[i], y[i] = map(int, input().split())

matrix = [[0] * (max(max(x), max(y)) + 10) for _ in range((max(max(x), max(y)) + 10))]

for i in range(N):
    for c in range(y[i], y[i] + 10):
        for r in range(x[i], x[i] + 10):
            if matrix[r][c] == 0:
                matrix[r][c] = 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]:
            total += 1

print(total)

