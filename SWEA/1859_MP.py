# 백만장자 프로젝트
while True:
    try:
        num = int(input())
        case = 1
        for _ in range(num):
            day = int(input())
            money = list(map(int, input().split()))
            total = 0
            

            for i in range(day):
                if money[i] < max(money[i:]):
                    total += (max(money[i:]) - money[i])
            print(f'#{case} {total}')
            case += 1
    except:
        break