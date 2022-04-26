'''
O(n^2)으로 해도 최대 10만번
'''
# 버블소트
def bubbleSort(lst):
    # len(lst) - 1까지 하면 맨 마지막 꺼가 검사가 안 됨
    for i in range(len(lst), 0, -1):
        for j in range(1, i):
            if lst[j-1] > lst[j]:
                tmp = lst[j-1]
                lst[j-1] = lst[j]
                lst[j] = tmp
    return lst


T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))

    nums = bubbleSort(nums)
    print(nums[7])

