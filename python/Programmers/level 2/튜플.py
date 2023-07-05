'''
튜플을 표현하는 집합이 주어지면 이를 보고 원래 튜플을 반환하는 문제
여기서의 튜플은 셀 수 있는 수량의 순서있는 요소들의 모음
'''

def solution(s):
    answer = []
    numbers = [0] * 100001
    numbers_set = set()
    
    # 숫자들 개수 계산
    n = ''
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            n += s[i]
        else:
            if n:
                numbers[int(n)] += 1
                numbers_set.add(int(n))
            n = ''
    
    numbers_rank = []
    numbers_set = list(numbers_set)
    
    # 튜플의 요소와 각 요소의 개수를 리스트에 담고 이를 내림차순 정렬
    for i in range(len(numbers_set)):
        number = numbers_set[i]
        numbers_rank.append((number, numbers[number]))
    
    numbers_rank.sort(key=lambda x: -x[1])
    
    for i in range(len(numbers_rank)):
        answer.append(numbers_rank[i][0])

    return answer