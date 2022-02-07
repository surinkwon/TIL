# ACM 호텔
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    if n % h:
        rlt = str(n%h)
        if n // h + 1 < 10:
            rlt += '0' + str(n//h+1)
        else:
            rlt += str(n//h+1)
    else:
        rlt = str(h)
        if n // h < 10:
            rlt += '0' + str(n//h)
        else:
            rlt += str(n//h)
    print(rlt)


