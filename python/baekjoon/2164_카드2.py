from collections import deque


'''
만약 N이 홀수면 처리를 해주지 않으면 짝수만 남게 되어 2부터 버리고 넘기는 작업을 함
그런데 실제로는 홀수를 버리고 짝수를 뒤로 넘기는 작업이 이루어지기 때문에
2는 뒤로 넘기게됨 따라서 맨 마지막 수를 앞에 하나 붙여줌

예: N이 5면 12345 -> 3452 -> 524 -> 42 -> 2 원래 작업은 이렇게 되는데 
홀수를 앞에 붙여주는 작업을 하지 않으면
24 -> 4
홀수를 앞에 붙여주면
524 -> 42 -> 2 이렇게 됨 따라서 내가 짠 로직에서는 N이 홀수일 때 앞에 홀수를 붙여줘야
제대로 작동함
'''

# 덱으로 구현
N = int(input())

# 1부터 버리고, 뒤로 넘기고를 반복하기 때문에 홀수는 모두 버려지게 됨
cards = deque([i for i in range(2, N + 1, 2)])


if N % 2:
    cards.appendleft(N)

while len(cards) > 1:
    cards.popleft()
    num = cards.popleft()
    cards.append(num)

print(cards[0])
