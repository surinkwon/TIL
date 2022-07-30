'''
피보나치 수 구하는 문제
'''

def solution(n):

# dp 풀이
#     fibo = [0, 1]
    
#     for i in range(2, n + 1):
#         fibo.append(fibo[i - 2] + fibo[i - 1])
    
# answer = fibo[n]

    fibo1 = 0
    fibo2 = 1
    
    for i in range(2, n + 1):
        if i % 2:
            fibo2 += fibo1
        else:
            fibo1 += fibo2
    
    if n % 2:
        answer = fibo2
    else:
        answer = fibo1
    
    return answer % 1234567