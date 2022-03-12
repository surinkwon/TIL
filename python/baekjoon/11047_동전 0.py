N, k = map(int, input().split())
num = 0

# 동전 가치를 담은 리스트를 만들고 그 뒤에서부터 읽어가면서
# 필요한 동전 개수를 세면 됨 
coins = [0] * N
for i in range(len(coins)):
    coins[i] = int(input())

for i in range(len(coins)-1, -1, -1):
    if k >= coins[i]:
        num += k // coins[i]
        k -= coins[i] * (k // coins[i])

print(num)