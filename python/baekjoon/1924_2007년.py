md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

M, D = map(int, input().split())
total = D
for i in range(M):
    total += md[i]

day = date[total % 7]
print(day)
