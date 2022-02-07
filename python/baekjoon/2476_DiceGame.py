# 주사위 게임
person = int(input())
rlt = []

for i in range(person):
    dice_lst = list(map(int, input().split()))
    dice_lst.sort()
    if dice_lst[0] == dice_lst[1] == dice_lst[2]:
        rlt.append(10000 + dice_lst[0] * 1000)
    elif (dice_lst[0] == dice_lst[1] and dice_lst[1] != dice_lst[2]) or (dice_lst[2] == dice_lst[1] and dice_lst[1]!= dice_lst[0]):
        rlt.append(1000 + dice_lst[1] * 100)
    else:
        rlt.append(dice_lst[2] * 100)

print(max(rlt))