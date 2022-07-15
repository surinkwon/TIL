'''
백트래킹
부분집합 만드는 것처럼 풀면 됨
부분집합을 만들다가 해당 집합의 합이 R을 넘어가면 더 검사하지 않도록 조건 지정
'''
def choosePro(i, N, s, p):
    global total
    if i == N:
        if R >= s >= L and max(p) - min(p) >= X:
            total += 1
    elif s > R:
        return
    else:
        p.append(problems[i])
        choosePro(i+1, N, s+problems[i], p)
        p.pop()
        choosePro(i+1, N, s, p)

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))

total = 0
choosePro(0, N, 0, [])

print(total)