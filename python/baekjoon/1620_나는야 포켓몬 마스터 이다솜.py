'''
딕셔너리로 안 하면 시간초과
'''

import sys

N, M = map(int, input().split())
dogam = [0] * (N + 1)
dogam_dict = {}

for i in range(1, N + 1):
    data = sys.stdin.readline().strip()
    dogam[i] = data
    dogam_dict[data] = i

for _ in range(M):
    data = sys.stdin.readline().strip()
    if '0' <= data[0] <= '9':
        print(dogam[int(data)])
    else:
        print(dogam_dict[data])