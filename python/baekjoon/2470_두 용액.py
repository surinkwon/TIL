'''
투포인터, 두 수의 합
'''

N = int(input())

solutions = sorted(list(map(int, input().split())))

p1, p2 = 0, N-1
sol1 = sol2 = 0
# 큰 값을 정말 아주 크게 해야함
min_d = 99999999999


while p1 < p2:
    # 두 수의 합이 음수면 0에 가깝게하려면 수를 키워줘야 함
    if solutions[p1]+solutions[p2] < 0:
        # 0에 더 가까운지 체크
        if min_d > abs(solutions[p1]+solutions[p2]):
            min_d = abs(solutions[p1]+solutions[p2])
            sol1 = solutions[p1]
            sol2 = solutions[p2]
        p1 += 1

    # 두 수의 합이 양수면 0에 가깝게하려면 수를 작게 해줘야 함
    elif solutions[p1]+solutions[p2] > 0:
        if min_d > abs(solutions[p1]+solutions[p2]):
            min_d = abs(solutions[p1]+solutions[p2])
            sol1 = solutions[p1]
            sol2 = solutions[p2]
        p2 -= 1
        
    else:
        sol1 = solutions[p1]
        sol2 = solutions[p2]
        break

print(sol1, sol2)