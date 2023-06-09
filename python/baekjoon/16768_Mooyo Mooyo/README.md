# [16768_Mooyo Mooyo](https://www.acmicpc.net/problem/16768)

# 처음 생각한 풀이법

- Puyo Puyo와 같지만 블록을 없애는 것을 4가 아닌 K일 때로 변경해서 풀이
    - board에서 블록이 있으면 bfs로 연결된 구간을 찾고 그 구간의 크기가 K 이상일 때 없앰
    - 중력을 적용해 블록을 아래로 떨어뜨림

# 틀렸다면 이후 풀이 방법 및 참고 자료

- 블록이 쌓여 있을 때 중간에 0으로 비어 있는 경우는 없기 때문에
    
    ```python
    for c in range(WIDTH):
            for r in range(N - 1, -1, -1):
                if board[r][c] and not v[r][c]:
                    can_disappear += removeCells(r, c, board[r][c])
                elif not board[r][c]:
                    break
    ```
    
    - 이런 식으로 0이 나오면 그 열은 더 이상 검사하지 않는 것으로 했는데 이로 인해 이상이 생겼다.
    - 이 방법이 틀린 이유
        - 중간에 끼어 있는 블록이 K개 이상 이어진 블록이라고 하면 이를 지우면 0이 된다. 그런데 그 위로 검사하지 않은 블록이 있을 수 있기 때문에 중간에 0이 있어도 검사를 멈추면 안 된다.