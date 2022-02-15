N = input()

i = str(int(N) - 1)
c = 0
mc = int(N)

while int(i) > 0:
    c += int(i)
    for j in i:
        c += int(j)
    
    if c == int(N):
        mc = min(mc, int(i))
        i = str(int(i)-1)
    else:
        i = str(int(i)-1)
    
    c = 0

if mc == int(N):
    print(0)
else:
    print(mc)