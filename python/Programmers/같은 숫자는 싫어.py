'''
배열에서 순서를 유지한 채 같은 숫자 중복을 제거하는 문제
'''

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            
    return answer