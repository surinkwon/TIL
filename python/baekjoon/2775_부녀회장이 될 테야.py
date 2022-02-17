tc = int(input())

# 아파트 배열
# 인덱스 에러 조심하기(인덱스 생각 똑바로)
apartment = [[i for i in range(1, 15)]] + [[0] * 14 for _ in range(15)]
for r in range(1, len(apartment)):
    for c in range(len(apartment[r])):
        if c == 0:
            apartment[r][c] = 1
        else:
            apartment[r][c] = apartment[r-1][c] + apartment[r][c-1]

for t in range(tc): 
    K = int(input())    # 층
    N = int(input())    # 호수

    print(apartment[K][N-1])

