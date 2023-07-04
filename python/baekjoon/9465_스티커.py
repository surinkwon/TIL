T = int(input())
HEIGHT = 2

for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for __ in range(HEIGHT)]
    DP = [[0] * N for __ in range(HEIGHT)]
    DP[0][0] = stickers[0][0]
    DP[1][0] = stickers[1][0]

    for c in range(1, N):
        for r in range(HEIGHT):
            # 변을 맞대고 있으면 찢어지기 때문에 현재 스티커에서 가장 큰 값은
            # 대각선 방향 스티커에서 현재를 더한 것과 이전 스티커 중에서 큰 값
            DP[r][c] = max(DP[r][c - 1], DP[(r + 1) % HEIGHT][c - 1] + stickers[r][c])
    
    print(max(DP[0][N - 1], DP[1][N - 1]))