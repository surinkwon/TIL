import sys

sys.stdin = open('input.txt')

T = int(input())

# 최대 리스트 길이를 구하는 함수
def max_len(lst):
    ml = 0
    for i in lst:
        if len(i) > ml:
            ml = len(i)

    return ml


for tc in range(1, T + 1):
    wall = [list(input()) for _ in range(5)]
    ml = max_len(wall)
    rlt = [''] * ml

    # 인덱스 에러가 나지 않도록 문자열 길이가 최대 문자열 길이보다 짧은 곳에는 0을 붙여줌
    for word in wall:
        if len(word) < ml:
            word.extend([0] * (ml - len(word)))

    # 세로로 읽는 거 인덱스 주의!! 헷갈리지 말고 똑바로 이해하고 쓰자
    # 열 별로 문자열을 만들어 최종 리스트에 저장하는 방식
    for c in range(ml):
        for r in range(5):
            if wall[r][c]:              # 세로로 읽으면서 해당 칸에 값이 있으면
                rlt[c] += wall[r][c]    # 최종 리스트에 더해줌

    print(f'#{tc} {"".join(rlt)}')

