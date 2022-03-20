from collections import deque

M = int(input())
N = int(input())

prime = deque()

for i in range(M, N + 1):
    # i가 2이하이면 n이 정의되지 않아서 nameerror가 나므로 주의
    if i > 2:
        for n in range(2, i):
            if i % n == 0:
                break
        if n == i - 1:
            prime.append(i)
    else:
        if i == 2:
            prime.append(2)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)