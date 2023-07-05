'''
수 포자 세명이 가각 답을 찍는 방법이 다른데 그 중 가장 많이 맞춘 사람을 반환하는 문제
1번째 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ...
2번째 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3 ...
3번째 수포자: 3, 3, 1, 1, 22, 4, 4, 5, 5, 3, 3, 1, 1...
'''

def solution(answers):
    rlt = []
    supoja = [0, 0, 0, 0]
    
    # 첫 번째 수포자 답 맞추기
    for i in range(len(answers)):
        if i % 5 == 0:
            if answers[i] == 1:
                supoja[1] += 1
        elif i % 5 == 1:
            if answers[i] == 2:
                supoja[1] += 1
        elif i % 5 == 2:
            if answers[i] == 3:
                supoja[1] += 1
        elif i % 5 == 3:
            if answers[i] == 4:
                supoja[1] += 1
        else:
            if answers[i] == 5:
                supoja[1] += 1
        
        # 두 번재 수포자 답 맞추기
        if i % 2:
            if i % 8 == 1 and answers[i] == 1:
                supoja[2] += 1
            elif i % 8 == 3 and answers[i] == 3:
                supoja[2] += 1
            elif i % 8 == 5 and answers[i] == 4:
                supoja[2] += 1
            elif i % 8 == 7 and answers[i] == 5:
                supoja[2] += 1
        elif answers[i] == 2:
            supoja[2] += 1
        
        # 세 번째 수포자 답 맞추기
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                supoja[3] += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                supoja[3] += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                supoja[3] += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                supoja[3] += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                supoja[3] += 1
    
    for s in range(1, 4):
        if max(supoja) == supoja[s]:
            rlt.append(s)
            
    return rlt