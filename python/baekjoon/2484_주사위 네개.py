people = int(input())
dices = []
dice_n = []
reward = []
for _ in range(people):
    dices.append(list(map(int, input().split())))

for person in dices:
    dice_n.append(list(set(person)))

for e in range(len(dices)):
    if len(dice_n[e]) == 1:
        reward.append(50000 + dice_n[e][0] * 5000)
    elif len(dice_n[e]) == 2:
        if dices[e].count(dice_n[e][0]) == 2 and dices[e].count(dice_n[e][1]) == 2:
            reward.append(2000 + dice_n[e][0] * 500 + dice_n[e][1] * 500)
        else:
            if dices[e].count(dice_n[e][0]) == 3:
                reward.append(10000 + dice_n[e][0] * 1000)
            else:
                reward.append(10000 + dice_n[e][1] * 1000)
    elif len(dice_n[e]) == 3:
        for dn in dice_n[e]:
            if dices[e].count(dn) == 2:
                reward.append(1000 + dn * 100)
    else:
        reward.append(max(dice_n[e]) * 100)

print(max(reward))