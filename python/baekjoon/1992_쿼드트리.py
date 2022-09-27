'''
영상을 4분할 해 압축하는 문제
재귀로 풀이
'''

# 압축하는 함수
def compression(v, n):
    global rlt

    cnt_one = cnt_zero = 0

    # 1, 0 개수 세기
    for i in range(n):
        for j in range(n):
            if v[i][j]:
                cnt_one += 1
            else:
                cnt_zero += 1
    
    # 압축할 수 없을 때
    if n > 1 and cnt_one and cnt_zero:
        # 4분할
        rlt += '('
        top_left = [[0] * (n // 2) for _ in range(n // 2)]
        top_right = [[0] * (n // 2) for _ in range(n // 2)]
        bottom_left = [[0] * (n // 2) for _ in range(n // 2)]
        bottom_right = [[0] * (n // 2) for _ in range(n // 2)]

        for i in range(n):
            for j in range(n):
                if i < n // 2 and j < n // 2:
                    top_left[i][j] = v[i][j]
                elif i < n // 2 and j >= n // 2:
                    top_right[i][j - (n // 2)] = v[i][j]
                elif i >= n // 2 and j < n // 2:
                    bottom_left[i - (n // 2)][j] = v[i][j]
                elif i >= n // 2 and j >= n // 2:
                    bottom_right[i - (n // 2)][j - (n // 2)] = v[i][j]

        compression(top_left, n // 2)
        compression(top_right, n // 2)
        compression(bottom_left, n // 2)
        compression(bottom_right, n // 2)

        rlt += ')'
    else:
        # 압축
        if cnt_one > cnt_zero:
            rlt += '1'
        elif cnt_zero > cnt_one:
            rlt += '0'


N = int(input())

video = [list(map(int, input())) for _ in range(N)]

rlt = ''

compression(video, N)

print(rlt)