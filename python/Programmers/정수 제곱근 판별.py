'''
정수가 주어지면 그것이 어떤 정수의 제곱인지 판별하는 문제
'''

def solution(n):
    answer = -1
    
    # n이 1 이상이므로 1일때도 판별하기 위해 n + 1
    for i in range(1, n + 1):
        if i ** 2 == n:
            answer = (i + 1) ** 2
            break
        elif i ** 2 > n:
            break
    
    return answer
