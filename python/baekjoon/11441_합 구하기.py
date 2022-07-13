'''
누적합
'''
import sys

N = int(input())
nums = [0] + list(map(int, sys.stdin.readline().split()))
M = int(input())

for n in range(2, N + 1):
    nums[n] += nums[n - 1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(nums[j]-nums[i-1])

