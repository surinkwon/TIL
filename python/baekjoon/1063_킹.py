direction = {'R': 0, 'L': 1, 'B': 2, 'T': 3, 'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7}
dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
w = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
h = [8, 7, 6, 5, 4, 3, 2, 1]

chess = [[0] * 8 for _ in range(8)]

pre_king, pre_stone, N = input().split()
chess[h.index(int(pre_stone[1]))][w.index(pre_stone[0])] = 's'
chess[h.index(int(pre_king[1]))][w.index(pre_king[0])] = 'k'
sr, sc = h.index(int(pre_stone[1])), w.index(pre_stone[0])
kr, kc = h.index(int(pre_king[1])), w.index(pre_king[0])

for _ in range(int(N)):
    d = direction[input()]
    nkr, nkc = kr + dr[d], kc + dc[d]
    
    if nkr == sr and nkc == sc:
        nsr = sr + dr[d] 
        nsc = sc + dc[d]
        if 0 <= nkr < len(chess) and 0 <= nkc < len(chess) and 0 <= nsr < len(chess) and 0 <= nsc < len(chess):
            chess[sr][sc], chess[kr][kc] = 0, 0
            chess[nsr][nsc], chess[nkr][nkc] = 's', 'k'
            sr, sc = nsr, nsc
            kr, kc = nkr, nkc

    else:
        if 0 <= nkr < len(chess) and 0 <= nkc < len(chess):
            chess[kr][kc] = 0
            chess[nkr][nkc] = 'k'
            kr, kc = nkr, nkc

for i in range(len(chess)):
    for j in range(len(chess)):
        if chess[i][j] == 's':
            stone = w[j] + str(h[i])
        if chess[i][j] == 'k':
            king = w[j] + str(h[i])

print(king)
print(stone)



