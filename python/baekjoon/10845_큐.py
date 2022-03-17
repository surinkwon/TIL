import sys

N = int(input())
queue = [0] * N
qf = qr = -1

for _ in range(N):
    data = list(sys.stdin.readline().split())
    if len(data) > 1:
        order = data[0]
        d = int(data[1])
    else:
        order = data[0]

    if order == 'push':
        qr += 1
        queue[qr] = d
    elif order == 'pop':
        if qf == qr:
            print(-1)
        else:
            qf += 1
            print(queue[qf])
    elif order == 'size':
        print(qr-qf)
    elif order == 'empty':
        if qf == qr:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if qf == qr:
            print(-1)
        else:
            print(queue[qf+1])
    else:
        if qf == qr:
            print(-1)
        else:
            print(queue[qr])


