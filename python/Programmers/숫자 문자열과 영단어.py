def solution(s):
    answer = ''
    
    alph = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    i = 0
    while i < len(s):
        # 숫자면 답에 더해줌
        if '0' <= s[i] <= '9':
            answer += s[i]
            i += 1
        else:
            # 문자면 문자를 식별하고 숫자로 바꿔서 답에 더해줌
            tmp = ''
            while i < len(s) and 'a' <= s[i] <= 'z':
                tmp += s[i]
                if alph.get(tmp):
                    answer += alph[tmp]
                    tmp = ''
                i += 1
            
    return int(answer)