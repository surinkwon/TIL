'''
숫자 n이 주어지면 연속된 수의 덧셈으로 해당 숫자를 만들 수 있는 경우의 수를 구하는 문제
이중 for문으로 쉽게 구현 가능
자기 자신은 항상 포함되므로 answer을 1로 시작
'''

def solution(n):
    answer = 1
    
    for start in range(1, n + 1):
        tmp = 0
        for cnt_num in range(start, n):
            tmp += cnt_num
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break

    return answer