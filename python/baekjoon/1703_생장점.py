while True:
    n = list(map(int, input().split()))
    if n[0] != 0:
        total = 1
        for i in range(1, n[0] * 2 + 1):
            if i % 2:
                total *= n[i]
            else:
                total -= n[i]
        print(total)
    else:
        break