'''
두 수의 최대공약수와 최소공배수를 구하는 문제
유클리드 호제법을 이용해 풀이
'''

def solution(n, m):
    answer = []
    
    # 큰 수와 작은 수 구분
    if n > m:
        big = n
        small = m
    elif n < m:
        big = m
        small = n
    else:
        return [n, n]
    
    # 큰 수가 작은 수로 나눠지면 작은 수가 최대공약수
    # 나눠지지 않으면 작은 수와 큰 수를 작은 수로 나눈 나머지를 두고 반복
    while big % small:
        tmp_big = big
        big = small
        small = tmp_big % small
    
    answer = [small, small * (n // small) * (m // small)]
    
    return answer