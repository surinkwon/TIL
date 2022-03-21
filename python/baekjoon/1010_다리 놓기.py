# 조합으로 풀면 됨
from math import factorial


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    rlt = factorial(M) / (factorial(M-N) * factorial(N))
    print(int(rlt))
