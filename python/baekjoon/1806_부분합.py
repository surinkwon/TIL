'''
투포인터, 구간합
'''

N, S = map(int, input().split())

nums = list(map(int, input().split()))
# 길이가 가장 작은 구간을 구하는 건데 p2를 1로 하면 길이가 1인 구간이 검사 안 될 수도 있음
p1 = p2 = 0
total = nums[p1]
min_len = N + 1

while p2 < len(nums):
    if total >= S:
        if min_len > p2 - p1 + 1:
            min_len = p2 - p1 + 1
        total -= nums[p1]
        p1 += 1

    else:
        p2 += 1
        if p2 < len(nums):
            total += nums[p2]

if min_len == N + 1:
    print(0)
else:
    print(min_len)