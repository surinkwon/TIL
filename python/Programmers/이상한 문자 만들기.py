'''
단어별로 짝수 글자는 대문자, 홀수 글자는 소문자로 만든 문자열을 반환하는 문제
아스키코드로 풀이
'''

def solution(s):
    answer = ''
    # 문자열에서의 인덱스가 아니라 단어별로 홀짝을 판별할 수 있도록 하는 변수
    word_index = 0

    for i in range(len(s)):

        # 단어를 구분
        if s[i] == ' ':
            word_index = 0
            answer += ' '
            continue
        
        # 단어별 홀수일 때
        if word_index % 2:
            if 'A' <= s[i] <= 'Z':
                answer += chr(ord(s[i])+32)
            else:
                answer += s[i]
        
        # 단어별 짝수일 때
        elif word_index % 2 == 0:
            if 'a' <= s[i] <= 'z':
                answer += chr(ord(s[i])-32)
            else:
                answer += s[i]
        
        word_index += 1
        
    return answer