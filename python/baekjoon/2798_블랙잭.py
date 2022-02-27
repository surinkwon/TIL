def p(lst, i, s, k):
    global max_total
    if i == 3:
        if max_total < s <= k:
            max_total = s
    elif s > k:
        return
    else:
        for j in range(i, len(lst)):     # 순열의 i번째 원소를 정해놓는 것임을 잊지 말자
            temp = lst[i]                # j는 항상 바뀌는 것이고 i가 정해진 것
            lst[i] = lst[j]
            lst[j] = temp
            p(lst, i + 1, s + lst[i], k) # 그래서 i번째 원소를 더하는 것
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

N, M = map(int,input().split())
cards = list(map(int, input().split()))
max_total = 0

p(cards, 0, 0, M)

print(max_total)
