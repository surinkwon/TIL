num = ''
while num != '0':
    num = input()
    total = 0
    for i in num:
        if i == '1':
            total += 2
        elif i == '0':
            total += 4
        else:
            total += 3
    if num != '0':
        print(total + len(num) + 1)
