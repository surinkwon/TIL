'''
문자열의 n번째 인덱스를 기준으로 정렬하는 문제
lambda식을 활용해 sort 메서드를 사용하면 쉽게 풀이 가능
'''

def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    
    answer = strings
    
    return answer