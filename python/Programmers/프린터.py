'''
중요도 순서를 분석해 원하는 문서가 언제 인쇄될지를 구하는 문제
'''

def solution(priorities, location):
    # 중요도 순서대로 정렬한 리스트 생성
    number_set = priorities[:]
    number_set.sort(reverse=True)
    
    max_pri_idx = 0
    cnt = print_idx = 0
    
    while True:
        # 내가 원하는 문서인지, 그것의 중요도가 가장 높은지를 구분
        if print_idx != location:
            if priorities[print_idx] == number_set[max_pri_idx]:
                cnt += 1
                max_pri_idx += 1
            else:
                priorities.append(priorities[print_idx])
        else:
            if priorities[print_idx] == number_set[max_pri_idx]:
                cnt += 1
                return cnt
            else:
                priorities.append(priorities[print_idx])
                location = len(priorities) - 1
        print_idx += 1
