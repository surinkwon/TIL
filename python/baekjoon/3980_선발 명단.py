'''
백트래킹
'''

import sys

def calAbilitySum(i, N, s):
    global max_ability_sum, v
    if i == N:
        if max_ability_sum < s:
            max_ability_sum = s
    elif i == 10 and max_ability_sum >= s + 100:
        return
    else:
        for j in range(11):
            if v[j] == 0 and ability[i][j]:
                v[j] = 1
                calAbilitySum(i+1, N, s+ability[i][j])
                v[j] = 0

T = int(input())

for _ in range(T):
    ability = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    max_ability_sum = 0
    v = [0] * 11

    calAbilitySum(0, 11, 0)
    print(max_ability_sum)