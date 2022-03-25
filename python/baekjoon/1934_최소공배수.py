'''
유클리드 호제법으로 최대공약수를 구하는 방법
1. 큰 수를 작은 수로 나눈다
2. 나머지가 0이라면 작은 수가 최대공약수
3. 나머지가 0이 아니라면 작은 수를 큰수로하고 나머지를 작은 수로 해서 2가 될 때까지 반복
'''
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    lg = max(a, b)
    sm = min(a, b)

    while lg % sm != 0:
        rest = lg % sm
        lg = sm
        sm = rest
    
    print(sm * (a // sm) * (b // sm))