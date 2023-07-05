'''
정렬 메소드를 사용하면 매우 쉬운 문제
입력받는 법만 알고 있으면 풀 수 있는 문제이다.
'''

def solution(s):
    answer = ''
    numbers = list(map(int, s.split()))
    
    numbers.sort()
    answer = f'{numbers[0]} {numbers[-1]}'
    return answer