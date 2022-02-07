# 주사위 쌓기

# 하나의 주사위에서 다음 주사위로 넘어갈 때 맞닿는 숫자를 반환하는 함수
def next_dice(lst, num):

    if lst.index(num) == 1:
        another_dn = lst[0]
    else:
        another_dn = lst[1]
    
    return another_dn
            
# 주사위를 하나씩 받고 서로 마주보는 눈 끼리 묶어서 저장
# 그 주사위 뭉치들을 차례대로 하나의 리스트에 저장
total_dice_pile = []
totals = []

dice_numbers = int(input())
for _ in range(dice_numbers):
    d = list(map(int, input().split()))
    each_dice = [[d[0], d[5]], [d[1], d[3]], [d[2], d[4]]]
    total_dice_pile.append(each_dice)

# 6번 반복하며 총 합을 구함(첫 번째 주사위는 어떤 면으로 시작하든 상관 없으므로 경우의 수 6개)
for first_num in range(1, 7): # 1부터 차례대로 바닥면에 닿도록 놓음
    dice_number = first_num
    total = 0
    for dice in total_dice_pile: # 아래 주사위부터
        for dice_pair in dice: # 주사위 속 눈들의 페어
            if dice_number in dice_pair: # 첫 번째 바닥에 놓이는 눈 혹은 맞닿는 면의 눈이 페어에 있다면
                dice_number = next_dice(dice_pair, dice_number) # 다음 주사위와 연결되는 눈을 저장
                dice_pair_index = dice.index(dice_pair) # 해당 페어의 인덱스를 저장
                
                # 해당 페어의 인덱스와 비교하여 다른 두 페어의 인덱스를 각각 저장
                if dice_pair_index == 0:
                    other_dice_pair_index = 1
                    another_dice_pair_index = 2
                elif dice_pair_index == 1:
                    other_dice_pair_index = 0
                    another_dice_pair_index = 2
                else:
                    other_dice_pair_index = 0
                    another_dice_pair_index = 1

        # 다른 페어들 중 가장 큰 값을 최종값에 더함
        total += max(max(dice[other_dice_pair_index]), max(dice[another_dice_pair_index]))
    totals.append(total)

print(max(totals))


