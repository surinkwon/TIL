# Baseball
t = int(input())
k = 0
y = 0

for _ in range(t):
    for __ in range(9):
        ye, ko = map(int, input().split())
        y += ye
        k += ko
    
    if k > y:
        print('Korea')
    elif k < y:
        print('Yonsei')
    else:
        print('Draw')
