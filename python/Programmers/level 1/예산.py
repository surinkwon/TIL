'''
정해진 예산으로 얼마나 많은 부서를 지원해줄 수 있는지 구하는 문제
부서가 원하는 예산을 정렬한 후 총 예산을 넘지 않는 구를 구하면 됨
'''

def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    
    for i in range(len(d)):
        total += d[i]
        
        if total > budget:
            break
            
        answer += 1
        
    return answer