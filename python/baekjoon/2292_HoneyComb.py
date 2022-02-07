# 벌집
num = int(input())
if num == 1:
    print(1)
else:
    num -= 1
    for i in range(1, num + 1):
        if num - i * 6 > 0:
            num -= (i * 6)
        else:
            print(i + 1)
            break
