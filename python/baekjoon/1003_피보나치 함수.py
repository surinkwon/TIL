'''
DP
'''
import sys
T = int(input())
fibo = [[1, 0], [0, 1]]
length = 2

for _ in range(T):
    N = int(sys.stdin.readline())
    if length <= N:
        while length <= N:
            fibo.append([fibo[length-1][0]+fibo[length-2][0], fibo[length-1][1]+fibo[length-2][1]])
            length += 1
    print(fibo[N][0], fibo[N][1])