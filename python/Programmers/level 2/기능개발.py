def solution(progresses, speeds):
    answer = []
    day = [0] * len(progresses)
    
    # 기능 개발까지 며칠 남았는지 구하기
    for i in range(len(progresses)):
        day[i] = (100 - progresses[i]) // speeds[i]
        
        if (100 - progresses[i]) % speeds[i]:
            day[i] += 1
    
    i = 0
    # 같은 날 배포할 수 있는 프로그램 수 구하기
    while i < len(day):
        cnt = 1
        j = i + 1
        
        # 이전 순서 기능보다 더 빨리 개발될 수 있으면 같이 배포
        while j < len(day) and day[i] >= day[j]:
            j += 1
            cnt += 1
            
        i = j
        answer.append(cnt)
        
    return answer