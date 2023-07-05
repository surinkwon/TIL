def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if (i + 2) * 2 + (yellow // i) * 2 == brown:
                answer = [i + 2, yellow // i + 2]
                break
        
    answer.sort(key=lambda x:-x)
    
    return answer