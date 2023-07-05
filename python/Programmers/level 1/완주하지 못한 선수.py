'''
한 명만 완주하지 못했으므로 이름순으로 정렬 후 이름이 서로 다른 곳이
완주하지 못한 사람이다.
'''

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    
    # 끝까지 이름이 다른 사람이 없었으면 참가자 중 마지막 이름의 참가자가 완주하지 못한 것
    if not answer:
        answer = participant[-1]
        
    return answer