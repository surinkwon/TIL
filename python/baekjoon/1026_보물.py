N = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(len(A)):
    total += A[i] * B[i]

print(total)