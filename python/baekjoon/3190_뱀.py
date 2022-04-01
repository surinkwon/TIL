'''
뱀 배열을 만들고 그걸 움직이면 되는데 어떻게 움직이냐면
머리를 우선 움직일지 결정하고 꼬리나 벽이랑 안 부딪혔으면 머리 옮기고 나머지 몸통, 꼬리는
앞의 인덱스의 값으로 바꿔주면 됨(실제로는 몸통 먼저 바꾸고 머리는 마지막에 바꿔줌)

처음에 접근하려고 했던 방식은 보드를 만들어놓고 거기에 뱀이 가는 길을 1로 표시해가면서
검사를 하는 것이었다. 그런데 이렇게하면 머리와 몸통들의 방향이 어디인지 구분하기가 어려웠다.
몸이 길어지면 머리와 몸통의 방향이 다를텐데 그것을 따로 저장해가면서 바꾸자니 너무 힘들 것 같았다.
그래서 다른 방법을 생각하다가 뱀이 움직이면 뒤쪽 몸통은 앞의 몸통이 있던 자리로 온다는 것이 생각났다.
따라서 굳이 모든 몸통의 방향을 따질 필요 없이 뱀 몸통의 인덱스만 가지고 뱀 자리를 구할 수 있음을 깨달았다.
이것을 생각해내기까지 오래 걸렸다. 이후는 큰 어려움 없이 풀었다.

주의할 점
- 조건 잘 읽기(뱀은 1,1부터 시작한다. 따라서 보드의 인덱스는 1부터 보드 크기만큼 있어야한다.)
- 위와 비슷한 맥락으로 범위 설정 주의
- 뱀의 몸통을 바꿀 때 앞쪽 인덱스부터 바꾸면 모든 몸통이 똑같은 인덱스를 가지게 된다. 따라서 꼬리부터 앞쪽으로 움직이도록 바꿔야 함
- 리스트 얕은 복사 일어나는 거 주의하자 제발. 웬만하면 그냥 리스트 통째로 할당하지 말고 변수로 따로 받아서 할당하자
'''
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0] * (N+1) for _ in range(N+1)]

# 보드에 사과가 있는 곳 표시
for i in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

L = int(input())
change = [0] * 1000000

# 방향을 바꾸는 시간과 방향을 저장
for i in range(L):
    tmp = list(input().split())
    change[int(tmp[0])] = tmp[1]

time = 0
snake = [[1, 1]]
d = 0

# 게임이 끝날 때까지
while True:
    time += 1
    head_r, head_c = snake[0]
    head_r += dr[d]
    head_c += dc[d]

    # 뱀 머리가 몸통과 부딛히지 않고, 벽에 닿지 않으면 간다
    if [head_r, head_c] not in snake and 0 < head_r < N + 1 and 0 < head_c < N + 1:
        # 간 곳에 사과가 없으면 그냥 움직인다
        if board[head_r][head_c] == 0:
            # 몸통 뒤부터 차례대로 움직이고
            if len(snake) > 1:
                for j in range(len(snake) - 1, 0, -1):
                    snake[j][0], snake[j][1] = snake[j - 1][0], snake[j - 1][1]
            # 마지막으로 머리 움직임
            snake[0][0] = head_r
            snake[0][1] = head_c
        # 사과가 있으면 먹고 자란다
        else:
            snake = [[head_r, head_c]] + snake
            board[head_r][head_c] = 0
    else:
        break
    
    # 방향을 바꾸는 시간이 오면 바꿔줌
    if change[time] == 'L':
        d = (d+1) % 4
    elif change[time] == 'D':
        d = (d+3) % 4

print(time)