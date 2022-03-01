month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    dmy = list(map(int, input().split()))
    total = 0

    if dmy[0]:
        # 윤년일 때
        if dmy[2] % 400 == 0 or (dmy[2] % 4 == 0 and dmy[2] % 100):
            for i in range(1, dmy[1]):
                if i == 2:
                    total += 1 # 2월을 넘어서면 하루 더 더해줌
                total += month[i]
            total += dmy[0]
            print(total)
        # 윤년이 아닐 때
        else:
            for i in range(1, dmy[1]):
                total += month[i]
            total += dmy[0]
            print(total)
    else:
        break



