'''
백트래킹
'''

def permu(i, n, nums):
    if i == n:
        for num in range(len(nums)):
            print(nums[num], end=' ')
        print()
    elif i > n:
        return
    else:
        for j in range(1, N + 1):
            if v[j] == 0:
                v[j] = 1
                permu(i+1, n, nums+str(j))
                v[j] = 0

N = int(input())
v = [0] * (N + 1)

permu(0, N, '')