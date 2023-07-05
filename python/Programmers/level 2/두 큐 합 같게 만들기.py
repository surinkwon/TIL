'''
하나의 큐에서 pop하고 다른 큐로 insert하는 것이 한 횟수이며 이걸 반복해서 
최소 몇 번만에 두 큐의 합을 같게할 수 있는지 횟수를 반환하는 문제
'''

from collections import deque

def solution(queue1, queue2):
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    cnt = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 큐 하나의 최대 길이가 30만이므로 두 큐의 모든 수를 한 번 돌 동안 합이 같아지지 않으면 같은 합을 만들 수 없음
    # 더 큰 합을 가진 큐에서 수를 pop해 다른 큐에 insert 이를 반복
    while cnt < 600000 and queue1_sum != queue2_sum:
        if queue1_sum > queue2_sum:
            first_num = queue1.popleft()
            queue2_sum += first_num
            queue1_sum -= first_num
            queue2.append(first_num)
        else:
            first_num = queue2.popleft()
            queue1_sum += first_num
            queue2_sum -= first_num
            queue1.append(first_num)
        cnt += 1
        
    if cnt >= 600000:
        answer = -1
    else: 
        answer = cnt
    
    return answer