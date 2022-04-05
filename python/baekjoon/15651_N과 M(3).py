'''
중복순열 구하기 
'''

def permu(sub):
    if len(sub) == M:
        for k in range(len(sub)):
            print(sub[k], end=' ')
        print()
    else:
        for j in range(1,N+1):
            sub.append(j)
            permu(sub)
            sub.pop()

N, M = map(int, input().split())
permu([])