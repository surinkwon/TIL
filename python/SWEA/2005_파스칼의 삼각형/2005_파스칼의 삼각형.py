import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    # 삼각형 배열 생성
    tri = [[0] * i for i in range(1, N + 1)]
    tri[0][0] = 1 # 삼각형의 맨 꼭대기는 항상 1

    for r in range(1, N):
        for c in range(len(tri[r])):
            # 삼각형의 양쪽 변이 아닐시 왼쪽과 오른쪽 위 숫자의 합을 저장
            if 1 <= c < len(tri[r]) - 1:
                # 실제 배열 상으로 보면 왼쪽 위와 바로 위가 됨
                tri[r][c] = tri[r - 1][c - 1] + tri[r - 1][c]
            else:
                tri[r][c] = 1 # 삼각형의 양쪽 변은 항상 1


    print(f'#{tc}')
    for i in range(N):
        print(' '.join([str(x) for x in tri[i]]))


