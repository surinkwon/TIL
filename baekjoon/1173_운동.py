N, m, M, T, R = map(int, input().split())
if M - m < T:
    print(-1)
else:
    total = 0
    p = m
    work_out = 0
    while work_out < N:
        if p + T <= M:
            p += T
            work_out += 1
            total += 1
        else:
            if p - R < m:
                p = m
                total += 1
            else:
                p -= R
                total += 1
    print(total)
