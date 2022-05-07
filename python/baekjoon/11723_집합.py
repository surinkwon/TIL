'''
셋으로 구현하면 시간초과
룩업 리스트로 하면 통과
'''
import sys

M = int(input())
tmp = [0] * 21

for _ in range(M):
    data = sys.stdin.readline().split()
    if data[0] == 'add':
        tmp[int(data[1])] = 1
    elif data[0] == 'check':
        if tmp[int(data[1])]:
            print(1)
        else:
            print(0)
    elif data[0] == 'remove':
        if tmp[int(data[1])]:
            tmp[int(data[1])] = 0
    elif data[0] == 'toggle':
        if tmp[int(data[1])]:
            tmp[int(data[1])] = 0
        else:
            tmp[int(data[1])] = 1
    elif data[0] == 'all':
        tmp = [1] * 21
    else:
        tmp = [0] * 21