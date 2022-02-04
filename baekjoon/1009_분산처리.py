import sys
t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if a % 10 in [1, 5, 6]:
        print(a % 10)
    elif a % 10 in [4, 9]:
        if b % 2:
            print(a % 10)
        else:
            print(a ** 2 % 10)
    elif a % 10 in [2, 3, 7, 8]:
        if b % 4 == 2:
            print((a ** 2) % 10)
        elif b % 4 == 3:
            print((a ** 3) % 10)
        elif b % 4 == 1:
            print(a % 10)
        else:
            print((a ** 4) % 10)
    else:
        print(10)