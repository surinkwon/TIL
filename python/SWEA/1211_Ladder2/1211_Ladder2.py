import sys

sys.stdin = open('input.txt')

T = 10
dr = [1, 0, 0]
dc = [0, 1, -1]

# 사다리 타고 내려가면서 이동 횟수 세는 함수
def lDistance(matrix, sp):
    copy_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)): # 깊은 복사해줌
        for j in range(len(matrix[0])):
            copy_matrix[i][j] = matrix[i][j]

    cnt = 0 # 이동 횟수
    r = 0   # 현재 행
    c = sp  # 현재 열
    d = 0   # 현재 방향

    while r != 99: # 미로 끝에 다다르면 종료
        copy_matrix[r][c] = 0
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
            if copy_matrix[nr][nc] == 1:
                r = nr
                c = nc
                cnt += 1

        d = (d+1) % 3

    return cnt


for tc in range(1, T + 1):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작점 찾기
    start = [0] * 50
    start_point = 0
    
    # 찾은 시작점들을 시작 배열에 넣어줌
    for i in range(len(ladder)):
        if ladder[0][i] == 1:
            start[start_point] = i
            start_point += 1
    
    # 시작 배열의 첫 인덱스가 0일 수도 있어서 미리 가장 작은 횟수를 시작점의 첫번째로 해줌
    min_dis = lDistance(ladder, start[0])
    min_dis_idx = start[0] # 가장 작은 횟수의 열번호

    idx = 1
    while start[idx]:
        dis = lDistance(ladder, start[idx])

        if min_dis > dis:
            min_dis = dis
            min_dis_idx = start[idx]

        idx += 1

    
    print(f'#{tc} {min_dis_idx}')

