'''
달팽이랑 같음 
'''

C, R = map(int, input().split())
K = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n = 0
d = 0
r, c = R, 0
d_r = R
d_c = C - 1

while n < C * R:
    for _ in range(d_r):
        if n == K:
            break
        r += dr[d]
        n += 1

    if n == K:
        break

    d = (d + 1) % 4
    d_r -= 1

    for _ in range(d_c):
        if n == K:
            break
        c += dc[d]
        n += 1
    
    if n == K:
        break

    d = (d + 1) % 4
    d_c -= 1

if n == K:
    print(c+1, R - r)
else:
    print(0)


