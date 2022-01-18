# 숫자의 개수
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

for i in mul:
    if i == '0':
        num[0] += 1
    elif i == '1':
        num[1] += 1
    elif i == '2':
        num[2] += 1
    elif i == '3':
        num[3] += 1
    elif i == '4':
        num[4] += 1
    elif i == '5':
        num[5] += 1
    elif i == '6':
        num[6] += 1
    elif i == '7':
        num[7] += 1
    elif i == '8':
        num[8] += 1
    else:
        num[9] += 1

for co in num:
    print(co)