'''
문제에 나와있는 그대로 구현
'''

# 문자열이 올바른 괄호 문자열인지 검사하는 함수
def isRightS(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return 0
            else:
                stack.pop()
    if stack:
        return 0
    return 1


def makeRight(s):
    # 빈 문자열이면 반환
    if s == '':
        return s

    # 올바른 괄호 문자열이어도 그냥 반환
    elif isRightS(s):
        return s

    else:
        ob_cnt = cb_cnt = 0
        u = ''
        v = ''

        # 앞부터 균형잡힌 괄호문자열을 구해서 u와 v로 나눔
        for i in range(len(s)):
            if s[i] == '(':
                ob_cnt += 1
            else:
                cb_cnt += 1
                
            if ob_cnt == cb_cnt:
                u = s[:i+1]
                v = s[i+1:]
                break
    
    # u가 올바른 괄호 문자열이면
    if isRightS(u):
        # v를 올바른 괄호 문자열로 만들고 u와 붙여서 반환
        v = makeRight(v)
        return u + v
    # u가 올바른 괄호 문자열이 아니면
    else:
        # v를 올바른 괄호 문자열로 만든 후 양쪽에 여는 괄호, 닫는 괄호를 붙임
        v = '(' + makeRight(v) + ')'

        # u는 양끝의 문자를 떼고
        tmp_u = u[1:len(u)-1]
        u = ''

        # 괄호를 뒤집음
        for i in range(len(tmp_u)):
            if tmp_u[i] == '(':
                u += ')'
            else:
                u += '('
        
        # v와 u를 붙여서 반환
        return v + u
                

def solution(p):
    answer = makeRight(p)
    return answer