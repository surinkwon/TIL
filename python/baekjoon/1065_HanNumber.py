# 한수
num = int(input())

a = [str(x) for x in range(101, num + 1)]

total = 0

if num < 100:
    total = num
elif num <= 1000:
    total += 99
    for i in a:
        if int(i[1]) - int(i[0]) == int(i[2]) - int(i[1]):
            total += 1

print(total)

