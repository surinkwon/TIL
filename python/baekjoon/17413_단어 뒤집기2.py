'''
문자열을 읽어가며 작업
공백은 그냥 출력
'<', '>'이 없으면 공백이나 괄호가 나올때까지 거꾸로 출력
'''

S = input()
rlt = ''

i = 0
# 문자열 범위 내에서
while i < len(S):
    # 현재 문자가 공백이면 결과 문자열에 더해줌
    if S[i] == ' ':
        rlt += S[i]
        i += 1
    # 만약 꺽쇠 괄호면 닫는 괄호가 나올 때까지 문자열에 더해줌
    elif i < len(S) and S[i] == '<':
        while i < len(S) and S[i] != '>':
            rlt += S[i]
            i += 1
        # 닫는 괄호 전까지 더하기 때문에 닫는 괄호까지 더해주고 한 칸 앞으로 감 
        rlt += S[i]
        i += 1
    else:
        # 그냥 문자열이면 첫번째 인덱스 저장
        fst = i
        # 공백이나 괄호가 나오기 전까지 인덱스 늘려줌
        while i < len(S) and S[i] != ' ' and S[i] != '<':
            i += 1
        last = i - 1

        # 문자열의 마지막부터 첫번째까지 더해줌
        while last >= fst:
            rlt += S[last]
            last -= 1

print(rlt)