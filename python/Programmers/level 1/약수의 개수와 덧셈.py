'''
두 수 사이에 있는 모든 수들의 약수의 개수를 구해서
약수의 개수가 홀수면 빼고, 짝수면 더한 수를 반환하는 문제
'''

# 약수 개수 구하는 함수
def findDivisor(number):
    end = int(number ** (1 / 2))
    cnt = 1
    
    for divisor in range(1, end + 1):
        if number % divisor == 0:
            cnt += 1
    
    cnt *= 2
    
    if end ** 2 == number:
        cnt -= 1
    
    return cnt

def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        divisor_cnt = findDivisor(num)
        
        if divisor_cnt % 2:
            answer -= num
        else:
            answer += num
        
    return answer