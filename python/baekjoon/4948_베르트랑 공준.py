'''
에라토스테네스의 체
파이썬으로 돌리면 시간초과, 파이파이로 돌리면 됨
'''

while True:
    N = int(input())
    if N:
        lst = [1] * (N * 2 + 1)
        cnt = 0

        for i in range(1, len(lst)):
            if i == 1:
                continue
            if lst[i]:
                if i > N:
                    cnt += 1
                for j in range(i, len(lst), i):
                    if i != j:
                        lst[j] = 0
        print(cnt)
    else:
        break