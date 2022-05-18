'''
백트래킹
'''

def makeMaxValue(i, n, numbers, s):
    global max_value, v
    if i == n:
        if max_value < s:
            max_value = s
    elif i > n:
        return
    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                numbers.append(nums[j])
                if i > 0:
                    makeMaxValue(i+1, n, numbers, s+abs(numbers[i-1] - numbers[i]))
                else:
                    makeMaxValue(i+1, n, numbers, s)
                numbers.pop()
                v[j] = 0

N = int(input())
nums = list(map(int, input().split()))
v = [0] * N
max_value = 0

makeMaxValue(0, N, [], 0)

print(max_value)
