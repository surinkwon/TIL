# 모든 경우의 수 고려...
# 각각의 블록 함수들을 다 만들어줬다... 미련하지만 지금은 이렇게밖에 못 풀겠다.. ㅜㅜ
def ilja(matrix, r, c):
    num_sum1 = num_sum2 = 0

    if c + 3 < len(matrix[0]):
        num_sum1 = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r][c + 3]
    if r + 3 < len(matrix):
        num_sum2 = matrix[r][c] + matrix[r + 1][c] + matrix[r + 2][c] + matrix[r + 3][c]

    return max(num_sum1, num_sum2)

def nemo(matrix, r, c):
    num_sum = 0
    if r + 1 < len(matrix) and c + 1 < len(matrix[0]):
        num_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]
    return num_sum

def nieun(matrix, r, c):
    num_sum1 = num_sum2 = num_sum3 = num_sum4 = num_sum5 = num_sum6 = num_sum7 = num_sum8 = 0
    if r + 2 < len(matrix) and c + 1 < len(matrix[0]):
        num_sum1 = matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+2][c+1]
    if 0 <= r - 1 and c + 2 < len(matrix[0]):
        num_sum2 = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r-1][c+2]
    if 0 <= r - 2 and 0 <= c - 1:
        num_sum3 = matrix[r][c] + matrix[r-1][c] + matrix[r-2][c] + matrix[r-2][c-1]
    if r + 1 < len(matrix) and 0 <= c - 2:
        num_sum4 = matrix[r][c] + matrix[r][c-1] + matrix[r][c-2] + matrix[r+1][c-2]
    
    # 대칭
    if 0 <= r - 2 and c + 1 < len(matrix[0]):
        num_sum5 = matrix[r][c] + matrix[r][c+1] + matrix[r-1][c+1] + matrix[r-2][c+1]
    if r + 1 < len(matrix) and c + 2 < len(matrix[0]):
        num_sum6 = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c+2]
    if 0 <= r - 2 and c + 1 < len(matrix[0]):
        num_sum7 = matrix[r][c] + matrix[r-1][c] + matrix[r-2][c] + matrix[r-2][c+1]
    if 0 <= r - 1 and 0 <= c - 2:
        num_sum8 = matrix[r][c] + matrix[r][c-1] + matrix[r][c-2] + matrix[r-1][c-2]

    return max(num_sum1, num_sum2, num_sum3, num_sum4, num_sum5, num_sum6, num_sum7, num_sum8)


def rieul(matrix, r, c):
    num_sum1 = num_sum2 = num_sum3 = num_sum4 =0
    if r + 2 < len(matrix) and c + 1 < len(matrix[0]):
        num_sum1 = matrix[r][c] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+2][c+1]
    if 0 <= r - 1 and c + 2 < len(matrix[0]):
        num_sum2 = matrix[r][c] + matrix[r][c+1] + matrix[r-1][c+1] + matrix[r-1][c+2]

    # 대칭
    if r + 2 < len(matrix) and 0 <= c - 1:
        num_sum3 = matrix[r][c] + matrix[r+1][c] + matrix[r+1][c-1] + matrix[r+2][c-1]
    if  r + 1 < len(matrix) and c + 2 < len(matrix[0]):
        num_sum4 = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c+1] + matrix[r+1][c+2]
    
    return max(num_sum1, num_sum2, num_sum3, num_sum4)

def moeum(matrix, r, c):
    num_sum1 = num_sum2 = num_sum3 = num_sum4 = 0
    if r + 1 < len(matrix) and c + 2 < len(matrix[0]):
        num_sum1 = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c+1] + matrix[r][c+2]
    if 0 <= r - 2 and c + 1 < len(matrix[0]):
        num_sum2 = matrix[r][c] + matrix[r-1][c] + matrix[r-1][c+1] + matrix[r-2][c]
    if 0 <= r - 1 and 0 <= c - 2:
        num_sum3 = matrix[r][c] + matrix[r][c-1] + matrix[r-1][c-1] + matrix[r][c-2]
    if r + 2 < len(matrix) and 0 <= c - 1:
        num_sum4 = matrix[r][c] + matrix[r+1][c] + matrix[r+1][c-1] + matrix[r+2][c]
    
    return max(num_sum1, num_sum2, num_sum3, num_sum4)



N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for i in range(N):
    for j in range(M):
        te1 = ilja(paper, i, j)
        te2 = nemo(paper, i, j)
        te3 = nieun(paper, i, j)
        te4 = rieul(paper, i, j)
        te5 = moeum(paper, i, j)
        
        max_sum = max(max_sum, te1, te2, te3, te4, te5)

print(max_sum)