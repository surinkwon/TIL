'''
다이나믹프로그래밍
'''

N = int(input())
nums = list(map(int, input().split()))
increase = [1] * N
decrease = [1] * N

for i in range(1, len(nums)):
    # 전 수보다 크면 증가 배열에 개수를 더해줌
    if nums[i] > nums[i-1]:
        increase[i] += increase[i - 1]
    # 작으면 감소 배열에 개수를 더해줌
    elif nums[i] < nums[i - 1]:
        decrease[i] += decrease[i - 1]
    # 같으면 두 배열에 개수를 더해줌
    else:
        increase[i] += increase[i - 1]
        decrease[i] += decrease[i - 1]

max_length = max(max(decrease), max(increase))
print(max_length)
