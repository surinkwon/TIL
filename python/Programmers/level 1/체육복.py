'''
체육복을 도둑맞은 학생과 여벌의 체육복을 가진 학생이 주어졌을 때
가장 많은 학생에게 빌려줘서 수업을 들을 수 있는 최대 학생 수를 구하는 문제

여벌을 가져온 학생이 도둑맞을 수도 있기 때문에 이 경우도 고려해야 함
'''

def solution(n, lost, reserve):
    students = [0] * (n + 2)
    lost_st_set = set(lost)
    
    for i in range(len(reserve)):
        # 여벌을 가져온 학생이 도둑맞지 않았으면 여벌이 있다고 표시
        # 도둑맞았으면 빌려줄 수는 없지만 자신이 따로 빌릴 필요는 없으므로 도둑맞은 학생에서 삭제
        if reserve[i] not in lost_st_set:
            students[reserve[i]] = 1
        else:
            lost_st_set.remove(reserve[i])
    
    lost = list(lost_st_set)
    
    max_students = 0
    
    # 최대로 빌려줄 때 몇명이 수업을 들을 수 있는지 구하는 함수
    def borrow(i, N, s):
        nonlocal max_students, students
        
        if i == N:
            if max_students < n - N + s:
                max_students = n - N + s
        else:
            
            # 자신의 아래번호에서 빌릴 경우
            if students[lost[i]-1]:
                students[lost[i]-1] = 0
                borrow(i+1, N, s+1)
                students[lost[i]-1] = 1
            
            # 자신의 윗 번호애서 빌릴 경우
            if students[lost[i]+1]:
                students[lost[i]+1] = 0
                borrow(i+1, N, s+1)
                students[lost[i]+1] = 1
            
            # 빌리지 않을 경우
            borrow(i+1, N, s)
            
    
    borrow(0, len(lost), 0)
    
    return max_students