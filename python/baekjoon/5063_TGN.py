# TGN
test = int(input())

for t in range(test):
    r, e, c = map(int, input().split())
    pro1 = r # 광고 안 했을 때 수익
    pro2 = e - c # 광고 했을 때 수익

    if pro1 > pro2:
        print('do not advertise')
    elif pro1 < pro2:
        print('advertise')
    else:
        print('does not matter')