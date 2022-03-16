# 스택 구현 및 실행
import sys

N = int(sys.stdin.readline())
stack = [0] * (N+1)
top = 0

for _ in range(N):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push':
        top += 1
        stack[top] = data[1]
    elif data[0] == 'pop' or data[0] == 'top':
        if top:
            print(stack[top])
            if data[0] == 'pop':
                top -= 1
        else:
            print(-1)

    elif data[0] == 'size':
        print(top)
    else:
        if top == 0:
            print(1)
        else:
            print(0)


