'''
모든 음식의 스코빌 지수가 K 이상이 되도록 새로운 음식을 만들고 그 횟수를 반환하는 문제
python heapq 라이브러리를 이용해 풀이
'''

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    under_k = 0
    
    # 만들고자 하는 스코빌 지수 아래에 있는 음식의 개수
    for i in range(len(scoville)):
        if scoville[i] < K:
            under_k += 1
        else:
            break
    
    # 모든 음식의 스코빌 지수가 k가 될 때까지 새로운 음식 만들기
    while under_k > 0:

        # 음식이 하나밖에 남지 않았는데 스코빌 지수가 k가 안 되면 -1 반환
        if len(scoville) == 1:
            return -1
        
        # 가장 맵지 않은 음식 꺼내기
        not_spicy1 = heappop(scoville)
        not_spicy2 = heappop(scoville)
        
        if not_spicy1 < K:
            under_k -= 1
            
        if not_spicy2 < K:
            under_k -= 1
        
        # 새 음식 만들기
        new_food = not_spicy1 + not_spicy2 * 2
        
        if new_food < K:
            under_k += 1
        
        heappush(scoville, new_food)
        answer += 1
    
    return answer