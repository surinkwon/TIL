import sys

N = int(input())
nums = [0] * (10001)

for i in range(N):
    num = int(sys.stdin.readline())
    # 아래처럼 1은 바로 프린트하도록 안 해주면 메모리 초과
    if num == 1:
        print(num)
    else:
        nums[num] += 1

for i in range(2, len(nums)):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)
    