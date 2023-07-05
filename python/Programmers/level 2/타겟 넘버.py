'''
dfs로 풀이(재귀로 구현)
'''

def solution(numbers, target):
    answer = 0
    
    def makeTarget(i, n, s):
        nonlocal answer

        # 모든 수를 더하거나 뺐으면 타겟 숫자가 됐는지 확인
        if i == n:
            if s == target:
                answer += 1
        else:
            # 현재 수를 더하는 경우
            makeTarget(i+1, n, s+numbers[i])

            # 현재 수를 빼는 경우
            makeTarget(i+1, n, s-numbers[i])
    
    makeTarget(0, len(numbers), 0)
    
    return answer