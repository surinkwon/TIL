num = int(input())
i = 1
total = 0

while True:
    if num - i >= 0:
        num -= i
        i += 1
    else:
        i = 1
        continue
    total += 1

    if num == 0:
        break

print(total)