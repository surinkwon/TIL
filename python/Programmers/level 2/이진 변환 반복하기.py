'''
문자열 s를 1이 될 때까지 다음과 같은 방법으로 변환며 변환 횟수와 제거된 0의 수를 세는 문제
1. 모든 0 제거
2. 모든 0이 제거된 문자열의 길이를 2진수로 변환 
'''
# 2진 변환 함수
def binaryChange(x):
    new_x = ''
    deleted_zero = 0
    
    # 0 제거
    for i in range(len(x)):
        if x[i] == '0':
            deleted_zero += 1
        else:
            new_x += '1'
    
    c = len(new_x)
    new_num = ''
    
    # 길이를 2진수로 변환
    while c != 0:
        new_num += str(c % 2)
        c //= 2
    
    return new_num, deleted_zero
        

def solution(s):
    change_num = deleted_zero_num = 0
    
    while s != '1':
        ns, zero_num = binaryChange(s)
        
        deleted_zero_num += zero_num
        change_num += 1
        
        s = ns
    
    answer = [change_num, deleted_zero_num]
    return answer