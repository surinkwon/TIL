'''
들어오거나 나간 기록에 따라 유저 아이디와 닉네임을 따로 저장해두고
닉네임이 바뀌면 해당 유저아이디의 닉네임을 변경해주고
마지막에 해당 유저 아이디의 닉네임과 출입기록을 이어주면 됨
'''

def solution(record):
    answer = []                                     # 출입기록
    userids = []                                    # 출입한 유저
    nickname = {}                                   # 유저의 닉네임
    
    for i in range(len(record)):
        data = list(record[i].split())
        if data[0] == 'Enter':                      # 들어온 기록이면
            answer.append('님이 들어왔습니다.')       # 들어온 대로 표시
            userids.append(data[1])                 # 해당 행위를 한 유저 기록
            nickname[data[1]] = data[2]             # 유저 닉네임 저장
        elif data[0] == 'Leave':                    # 나간 기록이면
            answer.append('님이 나갔습니다.')        # 나간 대로 표시
            userids.append(data[1])                 # 해당 유저 기록
        else:
            nickname[data[1]] = data[2]             # 닉네임 변경 기록이면 그냥 변경해줌
    
    for i in range(len(answer)):
        answer[i] = nickname[userids[i]] + answer[i]
    
    return answer