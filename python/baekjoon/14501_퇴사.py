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
        howMany(i+schedule[i][0], s+schedule[i][1])
        howMany(i+1, s)



N = int(input())
schedule = [0] * N
for i in range(N):
    schedule[i] = list(map(int, input().split()))

max_income = -1
howMany(0, 0)

print(max_income)