N = input()
rlt = 'NO'

for i in range(1, len(N)):
    mul1 = mul2 = 1
    for f in range(i):
        mul1 *= int(N[f])
    for s in range(i, len(N)):
        mul2 *= int(N[s])
    
    if mul1 == mul2:
        rlt = 'YES'
        break

print(rlt)