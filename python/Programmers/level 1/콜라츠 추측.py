'''
콜라츠 추측을 구현하는 문제
어떤 수가 짝수면 2로 나누고 홀수면 * 3 + 1을 1이 될 때까지 하며
반복한 횟수를 반환 
'''

def solution(num):
    answer = 0
    cnt = 0
    
    while num != 1 and cnt < 500:
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        cnt += 1
    
    if cnt == 500:
        answer = -1
    else:
        answer = cnt
    
    return answer