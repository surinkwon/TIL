# 주사위 세개
dice_lst = list(map(int, input().split()))
dice_lst.sort()
if dice_lst[0] == dice_lst[1] == dice_lst[2]:
    print(10000 + dice_lst[0] * 1000)
elif (dice_lst[0] == dice_lst[1] and dice_lst[1] != dice_lst[2]) or (dice_lst[2] == dice_lst[1] and dice_lst[1]!= dice_lst[0]):
    print(1000 + dice_lst[1] * 100)
else:
    print(dice_lst[2] * 100)
