import sys

sys.stdin = open('input.txt')

T = 10


# 사다리 타고 내려가면서 이동 횟수 세는 함수
def lDistance(matrix, sp):
    r = cnt = 0 # 시작 행, 이동 횟수
    c = bc = sp # 시작 열, 비교 열
    down = right = 1 # 방향
    left = -1

    while r != len(matrix): # 행이 마지막에 도달하면 중단
        # 왼쪽 옆길이 인덱스 범위 내이고 움직이기 이전 열이 현재 열과 같거나 더 왼쪽일 때 옆으로 이동
        if 0 <= c + left and matrix[r][c + left] == 1 and bc >= c:
            c += left
            cnt += 1
            continue
        # 오른쪽 옆길이 인덱스 범위 내이고 움직이기 이전 열이 현재 열과 같거나 더 오늘쪽일 때 옆으로 이동
        elif c + right < len(matrix[r]) and matrix[r][c + right] == 1 and bc <= c:
            c += right
            cnt += 1
            continue

        bc = c # 아래로 가면 비교열 갱신
        r += down # 통로가 없으면 기본적으로 아래로 감
        cnt += 1

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
    min_dis_idx = start[0]  # 가장 작은 횟수의 열번호

    idx = 1
    while start[idx]:
        dis = lDistance(ladder, start[idx])

        if min_dis > dis:
            min_dis = dis
            min_dis_idx = start[idx]

        idx += 1

    print(f'#{tc} {min_dis_idx}')

