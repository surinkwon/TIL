num = int(input())
ball = 1
for _ in range(num):
    cups = list(map(int, input().split()))
    if ball == cups[0]:
        ball = cups[1]
    elif ball == cups[1]:
        ball = cups[0]

print(ball)