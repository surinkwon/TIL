import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    # 상자 개수, 반복 횟수
    N, Q = map(int, input().split())
    boxes = [0] * N

    # 반복하는 횟수동안 변경할 상자 인덱스
    c_b = [list(map(int, input().split())) for _ in range(Q)]
    i = 1 # 작업 번호

    for q in c_b:
        start = q[0] - 1    # 바꿀 상자의 첫 번째 인덱스
        end = q[1] - 1      # 바꿀 상자의 마지막 인덱스

        for box_index in range(len(boxes)):

            # 인덱스 범위 내의 상자를 작업번호로 만들어줌
            if start <= box_index <= end:
                boxes[box_index] = i

        i += 1  # 작업 횟수 추가

    print(f'#{tc} {" ".join([str(x) for x in boxes])}')

