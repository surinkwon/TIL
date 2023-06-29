N = int(input())
boxes = list(map(int, input().split()))
DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if boxes[i] > boxes[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))