n = int(input())
if n > 1:
    b = list(map(int, input().split()))
    print(max(b) * min(b))
else:
    c = int(input())
    print(c ** 2)