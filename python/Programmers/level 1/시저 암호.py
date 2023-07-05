'''
알파벳을 n칸 옆으로 민 암호를 반환하는 문제
알파벳을 아스키 코드로 바꾼 뒤 기준(a, A)으로부터 얼만큼 떨어져있는지 알면 
암호 변환 가능
'''

def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        # 대문자
        if 'A' <= s[i] <= 'Z':
            answer += chr(65+(ord(s[i])-65+n)%26)

        # 소문자
        elif 'a' <= s[i] <= 'z':
            answer += chr(97+(ord(s[i])-97+n)%26)
        
        # 공백
        else:
            answer += s[i]
    
    return answer