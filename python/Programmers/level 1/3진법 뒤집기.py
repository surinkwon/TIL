'''
자연수가 주어지면 3진법으로 바꾼 뒤 그 수를 뒤집어 10진법으로 변환하는 문제
'''

# 3진법으로 변환하는 함수
def trit(num):
    rlt = ''
    
    while num > 0:
        rlt = str(num % 3) + rlt
        num //= 3
    
    return rlt

# 뒤집힌 3진법 수를 10진법으로 변환하는 함수
def tritToDecimal(num):
    rlt = 0
    
    for i in range(len(num)):
        rlt += int(num[i]) * (3 ** i)
    
    return rlt


def solution(n):
    n = trit(n)
    
    # 계산을 편하게 하기 위해 뒤집는 과정 없이 바로 넘겨줌
    answer = tritToDecimal(n)
    
    return answer