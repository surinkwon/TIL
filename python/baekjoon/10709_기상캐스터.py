H, W = map(int, input().split())

sector = [list(input()) for _ in range(H)]
pre = [[-1] * W for _ in range(H)]

for i in range(H):
    c = -1
    for j in range(W):
        if sector[i][j] == 'c':
            c = j
            pre[i][j] = 0
        else:
            if c != -1:
                pre[i][j] = j - c
                
        print(pre[i][j], end=' ')
    print()

