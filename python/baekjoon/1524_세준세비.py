t = int(input())
import sys

for _ in range(t):
    i = input()
    if i == '':
        sj_n , sb_n = map(int, sys.stdin.readline().split())
        sj = sorted(list(map(int, sys.stdin.readline().split())))
        sb = sorted(list(map(int, sys.stdin.readline().split())))

        j = k = 0
        while j != sj_n and k != sb_n:
            if sj[j] < sb[k]:
                j += 1
            else:
                k += 1
        
        if j == sj_n:
            print('B')
        elif k == sb_n:
            print('S')
        else:
            print('C')
