def howShort(string, l):
    word = string[:l]       # 비교할 문자열
    rlt = ''                # 결과
    cnt = 1                 # 같은 문자열 개수
    i = l
    j = 0
    
    while i < len(string):
        point = i                           # 비교할 문자열을 지정하기 위해 i를 기억할 필요가 있음
        while i < len(string) and j < len(word) and string[i] == word[j]:
            i += 1                          # 비교할 문자열과 원래 있던 문자열이 같은지 비교
            j += 1
        if j == l:                          # 같으면 개수를 세어줌
            cnt += 1
            j = 0
        else:                               # 다르면
            if cnt == 1:                    # 개수가 1개면 그냥 단어를 결과에 더해줌
                rlt += word
            else:                           # 개수가 여러개면
                rlt += str(cnt) + word      # 개수도 더해줌
            word = string[point:point+l]    # 비교할 문자열 다시 지정
            cnt = 1                         # 개수 초기화
            i = point + l                   # 비교할 범위 지정
            j = 0                           # 문자열이 서로 다를 때도 j 초기화 해줘야 함
    
    # 마지막 문자열은 비교는 해도 결과에 반영이 안 되므로 결과 문자열에 다시 더해줌
    if cnt == 1:
        rlt += word
    else:
        rlt += str(cnt) + word

    return len(rlt)
    

def solution(s):
    answer = 987654
    for i in range(1, len(s) + 1):
        tmp = howShort(s, i)        # 문자열 압축

        if answer > tmp:            # 압축한 길이가 이전보다 짧으면 갱신
            answer = tmp
    
    return answer
