'''
2차원 배열 순회

첫 번째 오류
- 0일 때 처리를 제대로 해주지 않았다. 함수의 결과값으로 세 개를 받게 해놨는데
    0일 때는 하나만 받게 해놔서 다른 문제가 해결되었더라도 제대로 돌아가지 않았을 것

두 번째 오류
if not (i == ni and j == nj):
    v[ni][nj][d] += 1
이 조건문을 if i!= ni and j != nj라고 해서 v배열에 정확한 값이 들어가지 않아 육목을 처리하지 못함
내가 쓴 의미는 맨 처음 좌표와 같지 않을 때 라는 조건이었는데 저렇게 하면 제대로 되지 않음 or 조건을 줘야 했음

세 번째 오류
- 맨 왼쪽 돌을 출력하라 했는데 왼쪽 아래 대각선으로 가는 경우에는 현재 돌 위치와 맨 왼쪽 위치가 바뀌게 되는데
    그 처리를 해주지 않음

기본적으로는 방문배열을 두고 이전에 방문했다는 뜻은 이 돌이 중간에 놓여있다는 뜻이므로
해당 방향으로 뻗어갈 때 한 번이라도 방문한 적이 있으면 그 돌과 그 방향으로는 다시 체크하지 않음
'''

dr = [0, 1, 1, 1]
dc = [1, 0, -1, 1]

def check():
    v = [[[0] * 4 for _ in range(19)] for _ in range(19)]

    # 바둑판 돌기
    for i in range(19):
        for j in range(19):

            # 돌이 놓여 있으면
            if board[i][j]:

                # 우, 하, 하좌, 하우 방향 살핌
                for d in range(4):

                    # 해당 방향에 대한 체크를 한 번도 한 적이 없으면 
                    if v[i][j][d] == 0:
                        num = 0

                        # 해당 방향을 체크하면서 그곳에 놓인 다른 돌들을 방문했다고 체크
                        for k in range(19):
                            ni, nj = i + k * dr[d], j + k * dc[d]
                            if 0 <= ni < 19 and 0 <= nj < 19 and board[ni][nj] == board[i][j]:
                                num += 1
                                if not (i == ni and j == nj):
                                    v[ni][nj][d] = 1
                            else:
                                break
                        
                        # 하좌 방향을 빼고는 체크를 시작한 돌이 가장 왼쪽 혹은 위쪽 돌
                        if num == 5 and d != 2:
                            return board[i][j], i + 1, j + 1

                        # 따라서 하좌 방향 출력 결과를 조작해줌
                        elif num == 5 and d == 2:
                            return board[i][j], ni, nj + 2

    return 0, 0, 0


board = [list(map(int, input().split())) for _ in range(19)]


rlt, rlt_r, rlt_c = check()
if rlt:
    print(rlt)
    print(rlt_r, rlt_c)
else:
    print(rlt)
