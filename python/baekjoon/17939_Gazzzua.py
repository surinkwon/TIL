'''
코인의 가격을 알 때 얻을 수 있는 최대 수익을 구하는 문제
'''

N = int(input())

prices = list(map(int, input().split()))

max_profit = max_price = 0

for i in range(len(prices) - 1, -1, -1):
    if max_price < prices[i]:
        max_price = prices[i]
    elif max_price > prices[i]:
        max_profit += max_price - prices[i]

print(max_profit)