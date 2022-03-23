import sys

sys.stdin = open('input.txt')

T = int(input())


# 넣을 재료 정하는 함수
# 부분집합 구하는 함수랑 같음
def chooseFood(i, bit, s):
    global chosen

    if i == N:
        if bit.count(1) == s:
            f = []
            for j in range(len(bit)):
                if bit[j]:
                    f.append(j)
            chosen.append(f)
            return
        else:
            return

    else:
        bit[i] = 0
        chooseFood(i+1, bit, s)
        bit[i] = 1
        chooseFood(i+1, bit, s)


# 고른 재료로 음식 만들고 다른 재료로 음식 만든 다음 그 둘 차이 구하는 함수
def makeFood(ing, s):
    food = 0
    other_food = 0
    for j in range(len(s)):
        for k in range(len(s)):
            # 고른 재료들의 시너지를 더해 요리를 만듦
            if j in ing and k in ing:
                if k != j:
                    food += s[j][k]
            # 남은 재료들의 시너지를 더해 다른 요리를 만듦
            elif j not in ing and k not in ing:
                if k != j:
                    other_food += s[j][k]

    return abs(other_food - food)



for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    c = [0] * N

    chosen = []
    chooseFood(0, c, N // 2) # 재료를 골라서 chosen에 넣음

    foods = [0] * len(chosen)
    for i in range(len(chosen)):
        # 고른 재료로 요리 하나를 만들고 나머지 재료로 다른 요리를 만듦
        foods[i] = makeFood(chosen[i], synergy)

    print(f'#{tc} {min(foods)}')

