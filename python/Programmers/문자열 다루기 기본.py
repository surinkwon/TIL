'''
문자열의 길이가 4 또는 6이고 모두 숫자로 이루어져있는지 판별하는 문제
함수는 return을 하면 실행이 중지되므로 조건에 맞지 않을 때 return을 해주면 
쉽게 풀이 가능
'''

def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        answer = False
        return answer
    
    for i in range(len(s)):
        if not ('0' <= s[i] <= '9'):
            answer = False
            return answer
        
    return answer