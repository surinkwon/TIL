# 사각형들의 정보를 받음
sq1= list(map(int, input().split()))
sq2= list(map(int, input().split()))
sq3= list(map(int, input().split()))
sq4= list(map(int, input().split()))
squares = [sq1, sq2, sq3, sq4]

# 사각형 길이의 최대를 구해서 그 크기만큼의 그래프를 만듦
max_width = max(max(sq1), max(sq2), max(sq3), max(sq4))
gragh = [[0] * (max_width + 1) for _ in range(max_width + 1)]
total = 0

# 각 사각형이 그래프에서 차지하는 공간을 채워줌
for i in range(4):
    for r in range(squares[i][1], squares[i][3]):
        for c in range(squares[i][0], squares[i][2]):
            if gragh[r][c] == 0:
                gragh[r][c] = 1

for i in range(len(gragh)):
    for j in range(len(gragh[i])):
        total += gragh[i][j]

print(total)