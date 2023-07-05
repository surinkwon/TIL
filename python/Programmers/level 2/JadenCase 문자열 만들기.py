'''
공백문자 뒤에 오는 문자만 대문자, 그 외는 소문자로 된 문자열로 변환하는 문제
'''

def solution(s):
    answer = ''
    
    if 'a' <= s[0] <= 'z':
        answer += chr(ord(s[0])-32)
    else:
        answer += s[0]
    
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and 'a' <= s[i] <= 'z':
            answer += chr(ord(s[i])-32)
        elif s[i - 1] != ' ' and 'A' <= s[i] <= 'Z':
            answer += chr(ord(s[i])+32)
        else:
            answer += s[i]
    return answer