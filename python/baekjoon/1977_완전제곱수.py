M = int(input())
N = int(input())
total = 0
min_sq = 987654321

sq = [0] * 101
for i in range(len(sq)):
    sq[i] = i ** 2

for i in range(len(sq)):
    if sq[i] > N:
        break
    if sq[i] >= M:
        total += sq[i]
        if min_sq > sq[i]:
            min_sq = sq[i]
    
if total:
    print(total)
    print(min_sq)
else:
    print(-1)