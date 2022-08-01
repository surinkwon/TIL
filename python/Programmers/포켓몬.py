'''
포켓몬 종류가 담긴 리스트가 주어지고
이 중 반 마리의 포켓몬을 가져갈 수 있을 때 가장 많은 종류를 가져가는 경우
몇 종류를 가져갈 수 있는지를 판별하는 문제

세트로 중복을 없애면 몇 종류가 있는지 나오게 되고 이를 가져갈 수 있는 포켓몬 수와 비교하면 됨
'''

def solution(nums):
    pre_length = len(nums)
    nums = set(nums)
    
    if pre_length // 2 <= len(nums):
        answer = pre_length // 2
    else:
        answer = len(nums)
    return answer