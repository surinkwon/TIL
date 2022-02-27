'''
12
34  이렇게 꼭짓점의 번호가 있다고 침
'''

# 해당 칸에서 정사각형이 있는지 검사하는 함수
def isSquare(matrix, r, c, mr, mc): # 숫자행렬, 현재 행, 현재 열, 최대 행 수, 최대 열 수
    size = 0
    # 정사각형 검사기 때문에 일단 해당 행 내에서 같은 수가 있는지 찾음(2번 꼭짓점 찾기)
    for d in range(1, mc - c): 
        # 같은 수가 있다면(2번 꼭짓점을 찾았다면)
        if matrix[r][c + d] == matrix[r][c]:
            # 3번 꼭짓점이 있는지 검사하고 만약 있다면
            if r + d < mr and matrix[r + d][c] == matrix[r][c]:
                # 4번 꼭짓점까지 검사 후 있으면 사각형 사이즈 계산
                if matrix[r + d][c + d] == matrix[r][c]:
                    s = (d + 1) ** 2
                    if s > size:
                        size = s
        
    return size


N, M = map(int, input().split())
big_square = [list(map(int, input())) for _ in range(N)]
max_size = 0

# 각 칸을 돌면서 검사
for i in range(N):
    for j in range(M):
        size = isSquare(big_square, i, j, N, M)
        if max_size < size:
            max_size = size

if max_size == 0:
    max_size = 1

print(max_size)