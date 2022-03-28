from math import factorial


N, K = map(int, input().split())

rlt = factorial(N) // (factorial((N-K)) * factorial(K))
print(rlt)