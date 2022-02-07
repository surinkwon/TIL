#과자
k, n, m = map(int, input().split())
money = m - (k * n)
if money < 0:
    print(-money)
else:
    print(0)