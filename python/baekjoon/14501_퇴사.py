'''
그리디, 백트래킹
'''

def howMany(i, s):
    global max_income

    if i > N:
        return
    elif i == N:
        if max_income < s:
            max_income = s
    else:
        # 해당 일자의 상담자를 받는 경우와 받지 않는 경우
        howMany(i+schedule[i][0], s+schedule[i][1])
        howMany(i+1, s)


N = int(input())
schedule = [0] * N
for i in range(N):
    schedule[i] = list(map(int, input().split()))

max_income = -1
howMany(0, 0)

print(max_income)