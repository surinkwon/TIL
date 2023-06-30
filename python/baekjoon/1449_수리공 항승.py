N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()
cw = water[0]
cnt = 1

for i in range(N):

    # 테이프 길이보다 막을 길이가 길면 이전까지 막고 테이프 하나 더 사용
    if water[i] - cw + 1 > L:
        cnt += 1
        cw = water[i]

print(cnt)