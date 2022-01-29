# 주사위 게임
t = int(input())
ch = sa = 100

for _ in range(t):
    c, s = map(int, input().split())
    if c > s:
        sa -= c
    elif c < s:
        ch -= s

print(ch)
print(sa)
