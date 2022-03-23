import sys

sys.stdin = open('input.txt')

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 다른 방으로 가는 함수
def moveNum(matrix, start):
    v = [[0] * len(matrix) for _ in range(len(matrix))] # 방문리스트
    r, c = start[0], start[1]
    v[r][c] = 1

    while True:
        for d in range(5):

            if d == 4: # 주위에 1 큰 방이 없으면 여태까지 방문한 횟수 반환
                return v[r][c]

            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix):
                if matrix[nr][nc] == matrix[r][c] + 1:
                    v[nr][nc] = v[r][c] + 1
                    r = nr
                    c = nc
                    break


for tc in range(1, T + 1):
    N = int(input())
    room = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    # 최대 방번호
    min_room_num = 987654321
    max_move = 0

    # 첫번째 방부터 순회
    for i in range(1, len(room)):
        for j in range(1, len(room[i])):
            room_num = room[i][j]
            move = moveNum(room, (i, j))

            if max_move < move:
                max_move = move
                min_room_num = room_num
            
            # 가장 작은 방 번호를 방문 횟수가 같을 때만 바꿔야 한다는 것 주의
            elif max_move == move:
                if min_room_num > room_num:
                    min_room_num = room_num

    print(f'#{tc} {min_room_num} {max_move}')

