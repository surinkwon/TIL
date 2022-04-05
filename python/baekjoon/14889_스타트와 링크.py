'''
dfs로 최솟값 찾기
'''

def howMin(i, a, b):
    global min_d
    if len(a) == len(b) == N // 2:
        a_ab = b_ab = 0
        
        for k in range(len(a)):
            for l in range(len(a)):
                a_ab += S[a[k]][a[l]]
                b_ab += S[b[k]][b[l]]
        
        if min_d > abs(a_ab - b_ab):
            min_d = abs(a_ab - b_ab)
    elif len(a) > N // 2 or len(b) > N // 2:
        return
    else:
        a.append(i)
        howMin(i+1, a, b)
        a.pop()
        b.append(i)
        howMin(i+1, a, b)
        b.pop()


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_d = 98765432
howMin(0, [], [])

print(min_d)
