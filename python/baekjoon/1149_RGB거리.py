'''
DP
'''

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
min_cost = [[0] * 3 for _ in range(N)]
min_cost[0] = cost[0]

for i in range(1, N):
    for j in range(len(cost[0])):
        if j == 0:
            min_cost[i][j] = cost[i][j] + min(min_cost[i-1][1], min_cost[i-1][2])
        elif j == 1:
            min_cost[i][j] = cost[i][j] + min(min_cost[i-1][0], min_cost[i-1][2])
        else:
            min_cost[i][j] = cost[i][j] + min(min_cost[i-1][1], min_cost[i-1][0])

print(min(min_cost[N-1]))

