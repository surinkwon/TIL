'''
백트래킹
'''

def calMaxEnergy(n, s):
    global nums, max_energy
    if n == 2:
        if max_energy < s:
            max_energy = s
    else:
        for i in range(1, n-1):
            ns = s + nums[i-1] * nums[i+1]
            num = nums[i]
            nums.pop(i)
            calMaxEnergy(n-1, ns)
            nums.insert(i, num)


N = int(input())
nums = list(map(int, input().split()))
max_energy = 0

calMaxEnergy(N, 0)

print(max_energy)
