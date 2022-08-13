'''
2016년 a월 b일이 무슨 요일인지 반환하는 문제
2016년 1월 1일은 금요일이므로 금요일을 배열의 인덱스 1 자리에 두고 시작
'''

def solution(a, b):
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    total_day = 0
    
    if a == 1:
        total_day += b
    else:
        for i in range(1, a):
            total_day += month_day[i]
        total_day += b
    
    answer = week[total_day % 7]
    
    return answer