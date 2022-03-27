def bi(lst, n, key):
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == key:
            return 1, middle
        elif lst[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    
    return 0, 0

N = int(input())
sanggeun = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))
nums_dict = dict()

for i in range(M):
    count = nums_dict.get(nums[i])
    if count:
        print(count, end=' ')
    else:
        rlt, idx = bi(sanggeun, N, nums[i])
        if rlt:
            cnt = k = l = 1
            while idx-k >= 0 and sanggeun[idx-k] == nums[i]:
                cnt += 1
                k += 1
            while idx+l < N and sanggeun[idx+l] == nums[i]:
                cnt += 1
                l += 1
        else:
            cnt = 0
        nums_dict[nums[i]] = cnt
        print(cnt, end=' ')
