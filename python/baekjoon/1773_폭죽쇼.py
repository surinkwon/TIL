'''
pypy는 통과
python은 시간초과
'''

import sys

N, C = map(int, input().split())
time = [0] * (C + 1)
cnt = 0

for _ in range(N):
    s = int(sys.stdin.readline())
    for i in range(s, len(time), s):
        if time[i] == 0:
            time[i] = 1
            cnt += 1

print(cnt)