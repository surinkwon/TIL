import sys

sys.stdin = open('input.txt')

T = int(input())


def pickIngredients(i, n, ing1, ing2):
    global min_dif

    if i == n:
        if len(ing1) == len(ing2):
            dif = makeFoods(ing1, ing2)
            if min_dif > dif:
                min_dif = dif
        return
    elif len(ing1) > n // 2 or len(ing2) > n // 2:
        return
    else:
        ing1.append(i)
        pickIngredients(i+1, n, ing1, ing2)
        ing1.pop()
        ing2.append(i)
        pickIngredients(i+1, n, ing1, ing2)
        ing2.pop()


def makeFoods(lst1, lst2):
    food1 = food2 = 0
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            if i != j:
                food1 += synergy[lst1[i]][lst1[j]]
                food2 += synergy[lst2[i]][lst2[j]]

    return abs(food1 - food2)



for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_dif = 987654321

    pickIngredients(0, N, [], [])

    print(f'#{tc} {min_dif}')