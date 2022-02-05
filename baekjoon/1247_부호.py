import sys

for _ in range(3):
    num = int(sys.stdin.readline())
    total = 0

    for __ in range(num):
        total += int(sys.stdin.readline())
    
    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print(0)





