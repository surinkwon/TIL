import sys

sys.stdin = open('input.txt')

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c):
    global v
    q = [0] * (N * N)
    qr = 0
    qf = -1
    q[qr] = [r, c]
    v[r][c] = 1
    cnt = 1

    while qr != qf:
        qf += 1
        cr, cc = q[qf]

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            '''
            abs(room[nr][nc] - room[cr][cc]) == 1 and v[nr][nc] == 0 이 조건을 
            room[nr][nc] == room[cr][cc] + 1대신 추가하면 더 빨리 결과를 구할 수 있다.
            1차이가 나면 움직이기 때문에 1 낮은 값이나 높은 값으로 가다보면 최종적으로는 몇 번 움직이는지 알 수 있다.
            그런데 이렇게 하려면 따로 다시 배열을 만들어서 각 방에서의 수를 넣어주고
            거기에서 가장 작은 값을 반환할 수 있도록 따로 처리해줘야 한다.
            '''
            if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == room[cr][cc] + 1:
                qr += 1
                q[qr] = [nr, nc]
                v[nr][nc] = 1
                cnt += 1

    return cnt


for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    max_cnt = 0
    min_num = 9875654321

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                num = room[i][j]
                cnt = BFS(i, j)

                if max_cnt < cnt:
                    max_cnt = cnt
                    min_num = num
                elif max_cnt == cnt:
                    if min_num > num:
                        min_num = num

    print(f'#{tc} {min_num} {max_cnt}')