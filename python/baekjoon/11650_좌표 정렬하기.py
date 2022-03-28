import sys

N = int(input())
nums = [0] * N

for i in range(N):
    nums[i] = list(map(int, sys.stdin.readline().split()))

nums.sort(key=lambda x:(x[0], x[1]))

for i in range(N):
    print(nums[i][0], nums[i][1])
