# 달팽이는 올라가고 싶다
speed, fall, goal = map(int, input().split())
before_one_last_day = goal - speed
one_day = speed - fall
total = 0
if before_one_last_day % one_day:
    total += before_one_last_day // one_day + 2
else:
    total += before_one_last_day // one_day + 1
print(total)