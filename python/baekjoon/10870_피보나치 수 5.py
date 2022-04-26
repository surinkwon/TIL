'''
DP
'''

def findFibo(num):
    fibo = [0] * (num + 1)
    fibo[1] = 1

    for i in range(2, num + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
    return fibo[num]

N = int(input())
if N > 0:
    rlt = findFibo(N)
else:
    rlt = 0
print(rlt)