'''
n번 탈 때마다 n배로 요금이 늘어나는 놀이기구를 count번 탈 때
현재 가진 근액에서 얼마가 부족한지 구하는 문제
'''

def solution(price, money, count):
    total_price = 0
    
    for n in range(1, count + 1):
        total_price += price * n
    
    answer = total_price - money
    
    if answer < 0:
        answer = 0
    
    return answer