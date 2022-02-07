# 손익분기점
a, b, c = map(int, input().split())
bep = 1

while True:
    if c > b:
        print(a // (c - b) + 1)
        break
    else:
        print(-1)
        break