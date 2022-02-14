now = list(map(int, input().split(':')))
mission = list(map(int, input().split(':')))
rest = [0] * 3

for i in range(len(now)-1, 0, -1):
    if now[i] > mission[i]:
        rest[i] = 60 - now[i] + mission[i]
        now[i-1] += 1
    else:
        rest[i] = mission[i] - now[i]

if now[0] > mission[0]:
    rest[0] = 24 - now[0] + mission[0]
else:
    rest[0] = mission[0] - now[0]

for j in range(len(rest)):
    if rest[j] < 10:
        rest[j] = '0' + str(rest[j])
    else:
        rest[j] = str(rest[j])

print(':'.join(rest))

