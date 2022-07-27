'''
스택을 이용해 괄호가 짝이 맞는지 확인하는 문제
여는 괄호는 스택에 넣고 닫는 괄호를 만나면 여는 괄호를 하나 빼는 식으로 풀이
'''

def solution(s):
    stack = [0] * len(s)
    top = -1
    
    for i in range(len(s)):
        if s[i] == '(':
            top += 1
            stack[top] = '('
        else:
            if top < 0:
                return False
            else:
                top -= 1
    
    # 스택이 비지 않아도 짝이 맞지 않는 것이므로 False 반환
    if top != -1:
        return False
    
    return True