import sys
N = int(sys.stdin.readline())
prices = []

for _ in range(N):
    prices.append(int(sys.stdin.readline()))

prices.sort(reverse=True)
min_cost = 0

for i in range(N):
    if i % 3 != 2:
        min_cost += prices[i]
    
print(min_cost)