from collections import deque

sticks = deque([64])

X = int(input())
while sum(sticks) != X:
    # 이렇게 조건을 지정하는 이유는 맨처음 막대기를 자른 후 다른 막대기들은
    # 목표값보다 작으면 막대기 덱에 저장되어있어야 하는데 pop을 하면 저장되지 않기 때문에
    # 맨처음 막대기만 pop을 해줌
    if sticks[0] == 64:
        shortest_stick = sticks.pop()
    else:
        shortest_stick = sticks[len(sticks) - 1]

    while sum(sticks) + shortest_stick > X:
        shortest_stick //= 2
    
    sticks.append(shortest_stick)

print(len(sticks))
