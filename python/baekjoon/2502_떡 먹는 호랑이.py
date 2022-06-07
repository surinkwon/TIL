'''
DP
'''

def findNum():
    f = 'f'
    s = 's'
    days = [f, s] + [''] * (D - 2)

    for i in range(2, D):
        days[i] = days[i - 2] + days[i - 1] 

    f = days[-1].count('f')
    s = days[-1].count('s')

    rlt_a = rlt_b = 0

    for i in range(1, K + 1):
        for j in range(1, K + 1):
            if f * i + s * j == K:
                rlt_a = i
                rlt_b = j
                return rlt_a, rlt_b

D, K = map(int, input().split())
a, b = findNum()

print(a)
print(b)