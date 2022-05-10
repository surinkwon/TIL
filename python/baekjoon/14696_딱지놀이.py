def findWinner(ans, bns):
    for i in range(4, -1, -1):
        if ans[i] > bns[i]:
            return 'A'
        elif ans[i] < bns[i]:
            return 'B'
    
    return 'D'

N = int(input())

for _ in range(N):
    a = [0] * 5
    b = [0] * 5
    a_data = list(map(int, input().split()))
    b_data = list(map(int, input().split()))

    for i in range(1, a_data[0] + 1):
        a[a_data[i]] += 1
    for i in range(1, b_data[0] + 1):
        b[b_data[i]] += 1

    rlt = findWinner(a, b)
    print(rlt)


