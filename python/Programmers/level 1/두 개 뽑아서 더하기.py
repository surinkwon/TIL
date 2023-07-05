'''
두 수를 뽑아 더한 결과를 중복 없이 오름차순 정렬해서 반환하는 문제
부분집합 구하는 방식으로 풂
'''

def solution(numbers):
    answer = set()
    v = [0] * len(numbers)
    
    def findPlusNum(i, N, s, num):
        nonlocal v, answer

        if num == N:
            answer.add(s)
        
        # 인덱스 에러 방지
        elif num > N or i > len(numbers) - 1:
            return
        
        else:
            findPlusNum(i+1, N, s+numbers[i], num+1)
            findPlusNum(i+1, N, s, num)
    
    findPlusNum(0, 2, 0, 0)
    
    answer = list(answer)
    answer.sort()
    
    return answer