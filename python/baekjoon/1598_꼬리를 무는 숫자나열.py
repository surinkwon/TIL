import sys

nums = list(map(int, sys.stdin.readline().split()))
nums_w = []
nums_h = []
nums.sort()
for num in nums:
    if num % 4:
        nums_w.append(num // 4 + 1)
        nums_h.append(num % 4)
    else:
        nums_w.append(num // 4)
        nums_h.append(num % 4 + 4)
w = nums_w[1] - nums_w[0]
h = nums_h[1] - nums_h[0] if nums_h[1] - nums_h[0] >= 0 else -(nums_h[1] - nums_h[0])
print(w+h)