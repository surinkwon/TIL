'''
누적합
일부분의 합은 전체에서 남은 부분을 뺀 값과 같다.
그냥 배열을 돌도록 코드를 짜면 r, c가 최대 1000이고 q가 최대 10000이기 때문에 엄청나게 많은 연산을 해야할 수 있다.
그래서 시간초과가 났다...
누적합을 구해놓고 일부만 빼는 형식으로 구현하면 시간을 줄일 수 있다.
'''

import sys

R, C, Q = map(int, input().split())
picture = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 각 행마다 누적합을 구함
for r in range(R):
    for c in range(1, C):
        picture[r][c] += picture[r][c - 1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    s = 0

    for r in range(r1, r2 + 1):
        if c1 > 0:
            s += picture[r][c2] - picture[r][c1 - 1]
        else:
            s += picture[r][c2]
    
    print(s//((r2-r1+1)*(c2-c1+1)))