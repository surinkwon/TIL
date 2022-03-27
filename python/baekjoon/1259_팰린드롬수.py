# 회문 판별 함수
def pal(num, s, e):
    if s >= e:
        return 'yes'
    elif s + 1 == e:
        if num[s] == num[e]:
            return 'yes'
        else:
            return 'no'
    else:
        if num[s] == num[e]:
            return pal(num, s+1, e-1)
        else:
            return 'no'

while True:
    N = input()
    if N == '0':
        break
    else:
        rlt = pal(N, 0, len(N)-1)
        print(rlt)
