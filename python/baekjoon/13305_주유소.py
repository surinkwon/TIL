'''
현재 도시의 기름값이 앞으로 갈 도시의 기름값보다 작으면 
더 작은 기름값의 도시가 나오기 전까지 도로 길이만큼 기름을 채우면 됨
'''

N = int(input())
road_lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_total = road_lengths[0] * prices[0]

min_price = prices[0]

for i in range(1, len(road_lengths)):
    if min_price > prices[i]:
        min_price = prices[i]
    
    min_total += min_price * road_lengths[i]

print(min_total)