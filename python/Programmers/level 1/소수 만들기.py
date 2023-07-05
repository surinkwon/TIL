'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 수를 구하는 문제
에라토스테네스의 체를 이용해 풀이
'''

from itertools import combinations

def solution(nums):
    answer = 0
    num_lst = list(combinations(nums, 3))
    
    for i in range(len(num_lst)):
        num_lst[i] = sum(num_lst[i])
    
    is_prime = [1] * (max(num_lst) + 1)

    # 제곱근 까지만 검사하면 되므로 검사할 마지막 수를 지정
    end = int(len(is_prime) ** (1 / 2))
    
    # 가장 큰 수까지 소수 판별
    for i in range(2, end + 1):
        if is_prime[i]:
            for j in range(i + 1, len(is_prime)):
                if j % i == 0:
                    is_prime[j] = 0
    
    # 숫자들 중 소수가 몇 개 있는지 계산
    for num in range(len(num_lst)):
        if is_prime[num_lst[num]]:
            answer += 1
        
    return answer