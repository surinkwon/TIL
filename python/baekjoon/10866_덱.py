from collections import deque
import sys

N = int(input())
de = deque()


for _ in range(N):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push_front':
        de.appendleft(int(data[1]))
    elif data[0] == 'push_back':
        de.append(int(data[1]))
    elif data[0] == 'pop_front':
        if len(de):
            num = de.popleft()
            print(num)
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if len(de):
            num = de.pop()
            print(num)
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(de))
    elif data[0] == 'empty':
        if len(de):
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if len(de):
            print(de[0])
        else:
            print(-1)
    else:
        if len(de):
            print(de[len(de)-1])
        else:
            print(-1)

